from flask import Flask, render_template, redirect, request, make_response, session, g
from os import urandom
import sqlite3


# Create the APP
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True # Remove it in prod
app.config["SECRET_KEY"] = urandom(16)
app.url_map.strict_slashes = False


# Database connexion
db_file = 'sqlite.db'

def connect_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_file)
    return db


# Database deconnexion
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return redirect("/", 302)


# Home page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Home page
@app.route("/dungeon/<int(signed=True):damage>/<path:username>", methods=["GET"])
def dungeon(damage=30, username="Link"):
    return render_template("dungeon.html", damage=damage, username=username)


# Report page
@app.route("/report", methods=["GET", "POST"])
def report():
    # Init
    response = ""
    db = connect_db()
    cur = db.cursor()

    # Check session ID
    if "id" not in session:
        session["id"] = 11

    if request.method == "GET":
        # Generating response
        response = make_response(render_template("report.html"))

    elif request.method == "POST":
        # Checking if session ID already in the BDD
        presence = cur.execute(f"SELECT id FROM report WHERE id={session['id']}").fetchall()

        if len(presence) >= 1:
            response = make_response(render_template("report.html", result="failed"))
        else:
            # INSERT request
            url = request.form.get("url")

            # Check if valid url have been sent
            if url[:22] == "http://localhost:5000/":
                cur.execute("INSERT INTO report VALUES (?, ?);", (session["id"], url))
                db.commit()

                # Generating response
                response = make_response(render_template("report.html", result="done"))

            else:
                # Generating response
                response = make_response(render_template("report.html", result="wrong"))
    return response
