from flask import Flask, request, render_template
from process import main

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    errors = ""
    if request.method == "POST":
        limit = None
        protein = None
        try:
            limit = int(request.form["limit"])
        except ValueError:
            errors += "<p>invalid input.</p>\n".format(request.form["limit"])
        try:
            protein = int(request.form["protein"])
        except ValueError:
            errors += "<p>protein needs to be one of .</p>\n".format(request.form["protein"])
        if limit is not None and protein is not None:
            try:
                meal, calorie, recipe = main(limit, protein)
                if meal is None:
                    raise TypeError
                return render_template("result.html", meal=meal, calorie=calorie, recipe=recipe)
            except TypeError:
                errors += "<p>higher limit</p>\n".format(request.form["limit"])

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
