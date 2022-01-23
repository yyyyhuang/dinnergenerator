from flask import Flask, request
from process import index

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def web_page():
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
                meal, calorie, recipe = index(limit, protein)
                if meal is None:
                    raise TypeError
                return '''
                                    <html>
                                        <body>
                                            <p>Your Dinner iss {meal}</p>
                                            <p>The calories of the meal is {calorie}</p>
                                            <p>Here is the link of the recipe {recipe}</p>
                                            <p><a href="/">Click here to generate again</a>
                                        </body>
                                    </html>
                             '''.format(meal=meal, calorie=calorie, recipe=recipe)
            except TypeError:
                errors += "<p>higher limit</p>\n".format(request.form["limit"])

    return '''
            <html>
                <body>
                    {errors}
                    <p>1: Beef\n2: Pork\n3: Chicken\n4: Seafood</p>
                    <form method="post" action=".">
                        <p>Calorie Limit: <input name="limit" /></p>
                        <p>Protein Number:<input name="protein" /></p>
                        <p><input type="submit" value="Generate Dinner" /></p>
                    </form>
                </body>
            </html>
        '''.format(errors=errors)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
