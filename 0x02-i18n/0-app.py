#!/usr/bin/env python3
"""
Basic flask setup
"""

from flask import Flask, render_template, request
import flask_babel import Babel

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Returns the index.html """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
