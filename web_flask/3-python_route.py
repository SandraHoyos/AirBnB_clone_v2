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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
