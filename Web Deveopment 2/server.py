from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods =['POST','GET'])
def submit_form():
    data = request.form.to_dict()
    print(data)
    return render_template("./index.html")

#sage maker aws
