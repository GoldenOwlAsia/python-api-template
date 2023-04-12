from flask import Blueprint, make_response, render_template, current_app, Response
from app.blueprints.authentication.views.login import login


blueprint: Blueprint = Blueprint(
    'authentication',
    __name__,
    url_prefix="/auth",
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/123', view_func=login.as_view('myauth2'))
