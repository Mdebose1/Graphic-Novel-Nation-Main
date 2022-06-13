from flask import Blueprint

bp = Blueprint('posts', __name__, template_folder='posts', url_prefix='posts')

from .import routes, models