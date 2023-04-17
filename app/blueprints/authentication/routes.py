from flask import Blueprint, make_response, render_template, current_app, Response
from app.blueprints.authentication.views.login import login
from app.blueprints.authentication.views.register import register

blueprint: Blueprint = Blueprint(
    'authentication',
    __name__,
    url_prefix="/auth",
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/login', view_func=login.as_view('login'))
blueprint.add_url_rule('/register', view_func=register.as_view('register'))
