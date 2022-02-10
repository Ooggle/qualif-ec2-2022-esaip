from flask import Flask, render_template, make_response, request, redirect

# Create the APP
app = Flask(__name__)

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
    return render_template("index.html")


# Admin page
@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Init
    response = ""

    if request.method == "GET":
        response = render_template("admin.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Verify crendentials
        if username == "part4" and password == "_C4n_B3_":
            response = render_template("admin.html", login="flag")
        else:
            response = render_template("admin.html", login="failure")

    return response
