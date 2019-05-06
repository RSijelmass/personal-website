from app import app
from app import db
from app.forms import PostForm
from app.models import User, Post
from flask import render_template, flash, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    form = PostForm()
    user=User.query.get(1)
    if not user:
        user = User(username="n00bs4hire", email="moneypls@cashcow.com")

    if form.validate_on_submit():
        post = Post(body=form.post.data, author=user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))

    return render_template("index.html", title='Home Page', user=user,
                           form=form)
