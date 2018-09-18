from flask import render_template, url_for, redirect, flash, request, abort
from flask_login import login_required, login_user, logout_user, current_user

from thermos import app, db, login_manager
from .forms import BookmarkForm, LoginForm, SignupForm
from .models import User, Bookmark, Tag


@login_manager.user_loader
def load_user(userid):
	return User.query.get(int(userid))

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html", new_bookmarks = Bookmark.newest(5))


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

@app.context_processor
def inject_tags():
	return dict(all_tags=Tag.all)


# if __name__ == "__main__":
# 	app.run(debug=False)
	

