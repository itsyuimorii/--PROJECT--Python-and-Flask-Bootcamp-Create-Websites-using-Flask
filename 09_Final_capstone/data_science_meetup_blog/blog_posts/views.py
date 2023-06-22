from os import abort
from flask import render_template, request, Blueprint, url_for, redirect, flash 
from flask_login import current_user, login_required
from data_science_meetup_blog import db
from data_science_meetup_blog.models import BlogPost
from data_science_meetup_blog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)

class Error(Exception):
    """Base class for custom errors."""
    pass


class BlogPostCreationError(Error):
    """Error raised when there is an issue with creating a blog post."""
    pass


class BlogPostUpdateError(Error):
    """Error raised when there is an issue with updating a blog post."""
    pass


class BlogPostDeletionError(Error):
    """Error raised when there is an issue with deleting a blog post."""
    pass


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
    

    # BLOG POST (VIEW)  
    @blog_posts.route('/<int:blog_post_id>')
    def blog_post(blog_post_id):
    # get blog post by id or return 404
        blog_post = BlogPost.query.get_or_404(blog_post_id)
        return render_template(
            'blog_post.html', 
            title=blog_post.title,
            date=blog_post.date, 
            post=blog_post
        )
# UPDATE
@blog_post.route('/<int:blog_post_id/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm()


    if form.validate_on_submit():

        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blog_posts.blog_post',blog_post_id=blog_post.id))

    elif request.method = 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html',title='Updating',form=form)


# DELETE
@blog_post.route('/<int:blog_post_id/delete',methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))
