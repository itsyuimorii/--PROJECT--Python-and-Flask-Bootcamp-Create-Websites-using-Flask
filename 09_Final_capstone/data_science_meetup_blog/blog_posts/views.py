from flask import render_template, request, Blueprint, url_for, redirect, flash 
from flask_login import current_user, login_required
from data_science_meetup_blog import db
from data_science_meetup_blog.models import BlogPost
from data_science_meetup_blog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)


# CREATE
@blog_posts.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()
    # if form.validate_on_submit():
    try:
        if request.method == 'POST':
            blog_post = BlogPost(
                title=form.title.data,
                text=form.text.data,
                user_id=current_user.id
            )
            db.session.add(blog_post)
            db.session.commit()
            flash("Blog Post Created")
            return redirect(url_for('core.index'))
    except:
        flash("Error: Blog Post Not Created")

        return render_template('create_post.html', form=form)