## This is __init__ file

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views