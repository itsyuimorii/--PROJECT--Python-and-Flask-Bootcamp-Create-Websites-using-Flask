# data_science_meetup_blog/__init__.py
"""_summary_: The __init__.py file is the first file that is run when the app is started. It contains the app factory function that creates the app, and the app's configuration settings.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

 
'''Database Setup'''
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connects the app to the database
db = SQLAlchemy(app)
# Connects the app to the migration folder
Migrate(app,db)

'''Login Configs'''
# Create a login manager object
 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


'''Blueprints'''
from data_science_meetup_blog.core.views import core
from data_science_meetup_blog.users.views import users
from data_science_meetup_blog.error_pages.handlers import error_pages
from data_science_meetup_blog.blog_posts.views import blog_posts
 
app.register_blueprint(error_pages)
app.register_blueprint(core)

 

 
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)












