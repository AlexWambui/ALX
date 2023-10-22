#!/usr/bin/python3
"""Starts a Flask web application listening on: 0.0.0.0, port 5000"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a string HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Displays C followed by value of variable text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """Displays Python followed by value of the vairable text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """Displays 'n is a number' only if n is of type int"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
    "Display a HTML page only if n is of type int"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n=None):
    """Displays a html page if n if of type int"""
    if isinstance(n, int):
        if n % 2 == 0:
            even_or_odd = "even"
        else:
            even_or_odd = "odd"
        return render_template("6-number_odd_or_even.html", n=n, even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.run()
