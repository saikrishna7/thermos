import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

from .config import config_by_name

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

# Configure Authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

toolbar = DebugToolbarExtension()

# for displaying timestamps
moment = Moment()

def create_app(config_name):
	app=Flask(__name__)
	
	# app.config['SECRET_KEY']= b'F\xd5\xd7\x01)Wf%`\xee\xf7)!\xa0+\x173\xe2\xf1\x00\xd4\x0b;\xb8'

	# Configure database
	# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
	# app.config['DEBUG']=True

	app.config.from_object(config_by_name[config_name])
	db.init_app(app)
	login_manager.init_app(app)
	moment.init_app(app)
	toolbar.init_app(app)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix = '/auth')

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint, url_prefix = '/')

	from .bookmarks import bookmarks as bkm_blueprint
	app.register_blueprint(bkm_blueprint, url_prefix = '/bookmarks')

	return app