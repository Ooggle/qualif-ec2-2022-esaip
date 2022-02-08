from flask import Flask, render_template, make_response, request, redirect, session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True # Remove it in prod
app.config["SECRET_KEY"] = "40da48eaff725cd443dcd3bf2124f5b0"


# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return redirect("/", 302)


# Home page
@app.route("/", methods=["GET"])
def index():
    # Init
    return make_response(render_template("index.html", logged=session["logged"]))


# Home page
@app.route("/profile", methods=["GET"])
def profile():
    # Init
    if session["logged"] == True:
        return make_response(render_template("profile.html", logged=session["logged"], user=session))
    else:
        return make_response(render_template("login.html", login="profile", logged=session["logged"]))


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
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
            session["messages"] = {}
            return make_response(render_template("login.html", logged=session["logged"]))


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
