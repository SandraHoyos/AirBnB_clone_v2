#!/usr/bin/python3

"""
script that starts a Flask web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function that returns Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ function that returns HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ returns C followed by the value text variable """
    txt = text.replace('_', ' ')
    return "C {}".format(escape(txt))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
