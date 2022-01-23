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
            errors += "invalid input\n".format(request.form["limit"])
        try:
            protein = int(request.form["protein"])
        except ValueError:
            errors += "protein needs to be from the menu below.\n".format(request.form["protein"])
        if limit is not None and protein is not None:
            try:
                meal, calorie, recipe = main(limit, protein)
                if meal is None:
                    raise TypeError
                return render_template("result.html", meal=meal, calorie=calorie, recipe=recipe)
            except TypeError:
                errors += "No dish under this calories, Please enter a higher limit.\n".format(request.form["limit"])

    return render_template("index.html", errors=errors)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
