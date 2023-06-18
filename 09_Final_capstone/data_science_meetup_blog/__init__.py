
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

'''Database Setup'''
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


from data_science_meetup_blog.core.views import core
from data_science_meetup_blog.error_pages.handlers import error_pages

app. register_blueprint(error_pages)
app.register_blueprint(core)