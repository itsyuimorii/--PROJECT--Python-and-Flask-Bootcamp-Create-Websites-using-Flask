# users/views.py
 
from data_science_meetup_blog import db
from data_science_meetup_blog.models import BlogPost, User
from data_science_meetup_blog.users.forms import (LoginForm, RegistrationForm,UpdateUserForm)
from data_science_meetup_blog.users.picture_handler import add_profile_pic
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

users = Blueprint('users', __name__)

# register
@users.route('/register', methods=['POST','GET'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, 
                    password=form.password.data, 
                    username=form.username.data)
        
        db.session.add(user)
        db.session.commit()

        flash('Thanks for Registeration!', 'success')
        return redirect(url_for('user.login'))

    return render_template('register.html',form=form)

# login
@users.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # grab the user
        if user.check_password(form.password.data) and user is not None: # check the password

            login_user(user)
            flash('Log in Success!','success')
 
            next = request.args.get('next') # check if there is a next page

            if next == None or not next[0]=='/':
                next = url_for('core.index')
            
            return redirect(next)
        
        return render_template('login.html',form=form)

             
# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

# account (update UserForm)
@users.route('/account', methods=['POST','GET'])
@login_required 
def account():

    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            user_pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = user_pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!', 'success')
        return redirect(url_for('users.account'))
    
     
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename = 'profile_pics/' +current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)



# user`s list of Blog posts
@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('user_blog_posts.html',blog_posts=blog_posts,user=user)




