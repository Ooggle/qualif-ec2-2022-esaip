from flask import Flask, render_template, make_response, request, redirect, session
from base64 import b64encode
from os import urandom
import sqlite3


# Create the APP
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True # Remove it in prod
app.config["SECRET_KEY"] = urandom(16)


# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return redirect("/", 302)


# Home page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Home page
@app.route("/dungeon", methods=["GET"])
def dungeon():
    return render_template("dungeon.html")


# Report page
@app.route("/report", methods=["GET"])
def report():
    return render_template("report.html")
