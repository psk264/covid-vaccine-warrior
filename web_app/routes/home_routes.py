# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template, redirect, flash
from app.vaccine_warrior import vaccine_stop


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/vaccine_warrior")
def vaccine_finder():
    return render_template("vaccine.html")

@home_routes.route("/about")
def about():
    return render_template("about.html")


@home_routes.route("/getinput", methods=["GET", "POST"])
def search_result():
    print("FORM DATA: ", dict(request.form))
    request_data = dict(request.form)
    zip_code = request_data.get("zip_code")
    print("zip code: ", zip_code)
    results = vaccine_stop(zipcode=zip_code)
    print(results)
    if "Phone" in results:
        flash("Vaccine Information Generated Successfully!", "success")
        return render_template("search_result.html", zip_code=zip_code, results=results)
    else:
        flash(results, "danger")
        return redirect("/vaccine_warrior")
