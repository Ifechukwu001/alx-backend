#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Chooses the best language to be used"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello():
    """Renders index page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
