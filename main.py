from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("subscription.html"))
        response.set_cookie("user_name", contact_name)
        return response



@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/FakeBook")
def FakeBook():
    return render_template("FakeBook.html")

@app.route("/boogle")
def boogle():
    return render_template("boogle.html")

@app.route("/hairsaloon")
def hairsaloon():
    return render_template("homepage.html")



if __name__ == '__main__':
    app.run(debug=True)