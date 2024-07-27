#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function that returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Returns C <text>"""
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Returns Python <text>"""
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n=None):
    """Returns n is number (if it is)"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_is_number_template(n=None):
    """Returns n is number template (if it is)"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Returns Number odd or even (only if n is int)"""
    odd_even = "even" if int(n) % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
