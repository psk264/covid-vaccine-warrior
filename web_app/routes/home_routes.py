# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template
from app.vaccine_finder import vaccine_stop


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/home")
def index():
    return render_template("home.html")

@home_routes.route("/about")
def about():
    return render_template("about.html")

@home_routes.route("/")
@home_routes.route("/vaccine_finder")
def vaccine_finder():
    return render_template("vaccine.html")

@home_routes.route("/search_result", methods=["GET", "POST"])
def search_result():
    print("FORM DATA: ", dict(request.args))
    request_data = dict(request.args)
    country_code = request_data.get("country_code") or "US"
    zip_code = request_data.get("zip_code") or "20057"
    print("zip code: ", zip_code)
    results = vaccine_stop(zipcode=zip_code)
    print(results)
    return render_template("search_result.html", zip_code=zip_code, results=results)
