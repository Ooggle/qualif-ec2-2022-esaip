from flask import Flask, render_template, make_response, request, redirect, session, g
from base64 import b64encode
from os import urandom
import sqlite3


# Create the APP
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True # Remove it in prod
app.config["SECRET_KEY"] = urandom(16)


# Connect to sqlite db
db_file = 'sqlite.db'

def connect_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_file)
    return db

# Close database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return redirect("/", 302)


# robots.txt
@app.route("/robots.txt", methods=["GET"])
def robots():
    with open(file="robots.txt", mode="r") as file:
        response = make_response(file.read(), 200)
        response.mimetype = "text/plain"
    return response


# robots.txt
@app.route("/init.db", methods=["GET"])
def init_db():
    with open(file="init.sql", mode="r") as file:
        response = make_response(file.read(), 200)
        response.mimetype = "text/plain"
    return response


# Home page
@app.route("/", methods=["GET"])
def index():
    # Session init
    if "userID" not in session:
        session["userID"] = urandom(16)
    if "logged" not in session:
        session["logged"] = None

    return render_template("index.html", logged=session["logged"])


# Galery page
@app.route("/galery", methods=["GET", "POST"])
def galery():
    # Session init
    if "userID" not in session:
        session["userID"] = urandom(16)
    if "logged" not in session or session["logged"] == None:
        return redirect("/login", 302)

    # DB init
    db = connect_db()
    cur = db.cursor()

    if request.method == "POST":
        # Image info
        file = request.files['image']
        file_name = file.filename
        file_content = b64encode(file.read()).decode()
        file_length = len(file_content)

        # INSERT image in db
        cur.execute(f"INSERT INTO galery (file_name, userID, file_length, file_content) VALUES ('{file_name}', ?, ?, ?);", (session["userID"], file_length, file_content))
        db.commit()

    pictures = cur.execute(f"SELECT file_name, file_content FROM galery WHERE userID = ?", (session["userID"],)).fetchall()
    return render_template("galery.html", len=len(pictures), pictures=pictures, logged=True)


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    # Session init
    if "userID" not in session:
        session["userID"] = urandom(16)
    if "logged" not in session:
        session["logged"] = None
    elif session["logged"] == True:
        return redirect("/", 302)

    # Init
    response = ""

    if request.method == "GET":
        response = render_template("login.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "" or password == "":
            response = render_template("login.html", login="empty")
        elif len(username) > 15:
            response = render_template("login.html", login="to_long")
        else:
            cur = connect_db().cursor()
            verify = cur.execute(f"SELECT * FROM users WHERE password = ? and username = '{username}'", (password,)).fetchall()
            if len(verify) != 0:
                session["logged"] = True
                response = redirect("/galery", 302)
            else:
                response = render_template("login.html", login="fail")

    return response


# Logout page
@app.route("/logout", methods=["GET"])
def logout():
    session["logged"] = None
    return render_template("index.html", logged=session["logged"])
