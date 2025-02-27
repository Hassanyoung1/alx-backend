#!/usr/bin/env python3
"""
Flask App that integrates Babel
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from jinja2.ext import Extension

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Render index.html
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    """
    Entry point
    """
    app.run(host='0.0.0.0', port=5003, debug=True)
