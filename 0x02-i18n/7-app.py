#!/usr/bin/env python3
"""
App module
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Union
from pytz import timezone
import pytz.exceptions


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Class config app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


def get_user():
    """get user"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ get locale
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])
