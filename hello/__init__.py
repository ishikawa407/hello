from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('hello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from hello import views, errors, commands