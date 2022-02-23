from flask import Flask, request, redirect, render_template, make_response, session
from captcha.image import ImageCaptcha
from flask_session import Session
from base64 import b64encode
from random import randint
from os import urandom


# Create the APP
app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(16)
app.config["TEMPLATES_AUTO_RELOAD"] = True # Remove it on prod


# Server side session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Generate random captcha
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ09123456789"
def getCaptcha():
    image = ImageCaptcha(width = 280, height = 90)
    captcha_text = ""
    for i in range(8):
        captcha_text += alphabet[randint(0, len(alphabet)-1)]
    data = image.generate(captcha_text)
    return captcha_text, b64encode(data.getvalue()).decode()


# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return redirect("/", 302)

# Wordlist
@app.route("/wordlist", methods=["GET"])
def wordlist():
    with open(file="wordlist.txt", mode="r") as file:
        response = make_response(file.read(), 200)
        response.mimetype = "text/plain"
    return response

# Home page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session["captcha_text"], captcha_data = getCaptcha()
        return render_template("login.html", captcha=captcha_data)
    
    elif request.method == "POST":
        # New captcha
        captcha_text, captcha_data = getCaptcha()
        # Get user input
        username = request.form.get("username")
        password = request.form.get("password")
        captcha = request.form.get("captcha")
        # Verify captcha
        if captcha == session["captcha_text"]:
            session["captcha_text"] = captcha_text # Changing session content after check if user failed the captcha or not
            if username == "admin" and password == "letmein1":
                return render_template("login.html", captcha=captcha_data, login="flag")
            else:
                return render_template("login.html", captcha=captcha_data, login="failure_creds")
        else:
            session["captcha_text"] = captcha_text
            return render_template("login.html", captcha=captcha_data, login="failure_captcha")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
