#models.py  
from datetime import datetime

from data_science_meetup_blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    """_summary_: The User class defines the structure of the users table in the database."""

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128)) #128 characters long
    posts = db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):  
        return check_password_hash(self.password_hash,password)
    

    def __repr__(self):
        """_summary_: The __repr__ method defines how the model object will be represented when it is printed, here it returns the user's account name (username)."""
        return f"Username {self.username}"
 

class BlogPost(db.Model):
    """_summary_: The BlogPost class defines the structure of the blog_posts table in the database.
 
    """
    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        """_summary_: The __repr__ method defines how the model object will be represented when it is printed, here it returns the post's title."""
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"

