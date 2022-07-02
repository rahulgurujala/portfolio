from flask import Flask, render_template, request
from server.pdf_Downloader import Pdf


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template("page-cases.html")


@app.route("/single_project", methods=["GET", "POST"])
def single_project():
    links = []
    if request.method == "POST":
        pdf_title = request.form.get("pdf")
        links = Pdf(pdf_title)
        links = links.pdf()
    return render_template("page-case-detail.html", data=links)


@app.route("/contact-us")
def contact():
    return render_template("page-contact-detail.html")


@app.route("/login")
def login():
    return render_template("auth-login.html")


@app.route("/signup")
def signup():
    return render_template("auth-signup.html")


@app.route("/forget-password")
def forget():
    return render_template("auth-re-password.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("page-error.html")


if __name__ == "__main__":
    app.run(debug=True)


# nhi
