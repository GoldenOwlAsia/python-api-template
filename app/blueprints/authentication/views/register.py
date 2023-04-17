from flask.views import MethodView
from flask import jsonify, request
from flask import make_response, render_template
from app.ext.sqlalchemy.database import db_session
from app.blueprints.authentication.models.model import FlaskUser
import hashlib

class register(MethodView):

    def get(self):
        return make_response(
            render_template(
                "register.jinja2",
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
        if user:
            return jsonify({
                "message": "User does exist"
            }) 
        
        user_create = FlaskUser(
            username=username,
            password=hashlib.md5(password.encode()).hexdigest()
        )

        db_session.add(user_create)
        db_session.commit()
        
        return jsonify({
            "created": True
        })
