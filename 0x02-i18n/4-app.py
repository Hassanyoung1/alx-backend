#!/usr/bin/env python3
"""
force a particular locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from jinja2.ext import Extension

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    get locale
    """
    get_locale = request.args.get('locale')
    if get_locale in app.config['LANGUAGES']:
        return get_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    index function
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
