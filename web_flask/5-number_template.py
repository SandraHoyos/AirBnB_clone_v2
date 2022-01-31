#!/usr/bin/python3

"""
intializing flask web app to listen on 0.0.0.0:5000
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Display "Hello HBNB!"
    """
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """
    route /hbnb displays
    """
    return ('HBNB')


@app.route('/c/<text>')
def c(text):
    """
    replaces _ with spaces
    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def py(text="is cool"):
    """
    replaces _ with spaces
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>')
def number(n):
    """
    Return n if it is an integer
    """
    if isinstance(n, int):
        return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>')
def template(n):
    """
    routes number_templates with n integer
    """
    return (render_template('5-number.html', n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
