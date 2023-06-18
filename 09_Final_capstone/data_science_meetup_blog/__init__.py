# data_science_meetup_blog/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

 
'''Database Setup'''
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)

'''Login Configs'''
# Create a login manager object
login_manager = LoginManager()
# Connects the app to the login manager
login_manager.init_app(app)
# Sets the login view for the app
login_manager.login_view = 'users.login'

'''Blueprints'''
from data_science_meetup_blog.core.views import core
from data_science_meetup_blog.error_pages.handlers import error_pages

app. register_blueprint(error_pages)
app.register_blueprint(core)












