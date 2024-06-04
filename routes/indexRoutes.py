from flask import Blueprint, render_template

indexRoutes = Blueprint('indexRoutes', __name__)


@indexRoutes.route('/')
def index():
    return render_template('index.html')
