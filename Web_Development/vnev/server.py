from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("./index.html")

@app.route("/<username>")
def hello_world2(username=None):
    return render_template("./index.html", name=username)

@app.route("/<username>/<int:post_id>")
def hello_world3(username=None, post_id=None):
    return render_template("./index.html", name=username, post_id=post_id)

@app.route("/blog")
def blog():
    return "<p>These are my vies on Blog</p>"