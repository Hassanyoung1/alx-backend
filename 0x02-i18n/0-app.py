#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template, request
import flask_babel import Babel

app = Flask(__name__)

@app.route('/')
def index():
    """ Returns the index.html """
    return render_template('/0-index.html')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
