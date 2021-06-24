# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")

@home_routes.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))

    name =  "Snow"
    message = f"Hello, {name}!"
    #return message
    return render_template("hello.html", message=message, othervar="abc123")
