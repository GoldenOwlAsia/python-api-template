# https://flask.palletsprojects.com/en/2.1.x/views/#method-based-dispatching

from flask.views import MethodView
from flask import jsonify, request
from flask import make_response, render_template
from app.ext.sqlalchemy.database import db_session
from app.blueprints.authentication.models.model import FlaskUser
import hashlib

class login(MethodView):

    def get(self):
        return make_response(
            render_template(
                "login.jinja2",
            )
        )

    def post(self):
        username = request.form["email"]
        password = request.form["password"]
        
        user = db_session.query(
            FlaskUser
        ).filter_by(
            username=username
        ).first()
        if not user:
            return jsonify({
                "message": "User not found"
            }) 

        password = hashlib.md5(password.encode()).hexdigest()
        if user.password != password:
            return jsonify({
                "message": "Incorrect Password"
            }) 

        return jsonify({
            "message": "login successfully"
        })
