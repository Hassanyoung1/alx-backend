#!/usr/bin/env python3
"""
Module for trying out Babel i18n
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Render the index template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    """
    Entry point
    """
    app.run(port="5000", host="0.0.0.0", debug=True)
