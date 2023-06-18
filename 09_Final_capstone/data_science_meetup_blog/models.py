#models.py  
from data_science_meetup_blog import db,login_manager
 
class User(db.Model):
    """_summary_: User model for database, inherits from db.Model, which is the base class for all models from SQLAlchemy, and UserMixin, which provides default implementations for the methods that Flask-Login expects user objects to have.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('BlogPost',backref='author',lazy=True) 


class BlogPost(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """

    pass