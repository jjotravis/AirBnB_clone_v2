#!/usr/bin/python3
"""
Starts Flask framework
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """home route
    return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """/hbnb route
    return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """/c/<text> route
    return 'C' + given text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def p_text(text="is cool"):
    """/python/<text>
    return 'Python + given text'"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """/number/<n> route
    Display n iff it's an integer"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """/number_template/n route
    return a HTML page with number in H1"""
    return render_template('5-number.html', name=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
