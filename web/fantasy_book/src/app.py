from flask import Flask, render_template_string, render_template, make_response, request, redirect, session
from os import urandom
from re import sub

# Flag is located to /flag.txt

# Create the APP
app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(16)

# Secure input
def secure(s):
    r = ["{{", "}}", "{%", "%}", "\.[a-zA-Z]", "import", "os", "system", "self", '\["', " "]
    for elem in r:
        s = sub(elem, "", s)
    return s


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


# Home page
@app.route("/", methods=["GET"])
def index():
    # Init
    if "logged" not in session:
        session["logged"] = None
    return make_response(render_template("index.html", logged=session["logged"]))


# Home page
@app.route("/profile", methods=["GET", "POST"])
def profile():
    # Init
    if "logged" not in session:
        session["logged"] = None

    if session["logged"] == True:
        pic = secure(session["picture"])
        desc = render_template_string(f"What a cool user picture #{pic}") 

        if request.method == "GET":
            return make_response(render_template("profile.html", logged=session["logged"], desc=desc, user=session))

        elif request.method == "POST":
            message = request.form.get("message")

            if message == "":
                return make_response(render_template("profile.html", logged=session["logged"], desc=desc, user=session, post="empty"))
            else:
                session["messages"] = session["messages"] + [message] # bug on append not getting saved after each posts
                return make_response(render_template("profile.html", logged=session["logged"], desc=desc, user=session))
    else:
        return redirect("/login", 302)


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if "logged" not in session:
        session["logged"] = None

    if request.method == "GET" and session["logged"]:
        return redirect("/profile", 302)
    elif request.method == "GET":
        return make_response(render_template("login.html"))

    elif request.method == "POST":
        username = request.form.get("username")
        age = request.form.get("age")
        sexe = request.form.get("sexe")
        picture = request.form.get("picture")
        description = request.form.get("description")

        # Check if not empty
        if username == "" or age == "" or sexe == "" or picture == "" or description == "":
            return make_response(render_template("login.html", login="empty", logged=session["logged"]))
        else:
            session["logged"] = True
            session["username"] = username
            session["age"] = age
            session["sexe"] = sexe
            session["picture"] = picture
            session["description"] = description
            session["messages"] = []
            return redirect("/profile", 302)


# Logout page
@app.route("/logout", methods=["GET"])
def logout():
    session["logged"] = None
    session["username"] = None
    session["age"] = None
    session["sexe"] = None
    session["picture"] = None
    session["description"] = None
    session["messages"] = None
    return make_response(render_template("index.html", logged=session["logged"]))


# Backup
@app.route("/backup", methods=["GET"])
def backup():
    with open(file="app.py", mode="r") as file:
        response = make_response(file.read(), 200)
        response.mimetype = "text/plain"
    return response
