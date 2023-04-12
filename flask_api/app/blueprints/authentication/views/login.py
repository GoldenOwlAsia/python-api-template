# https://flask.palletsprojects.com/en/2.1.x/views/#method-based-dispatching

from flask.views import MethodView
from flask import jsonify, request


class login(MethodView):

    def get(self):
        return jsonify({
            "hello": "world"
        })

    def post(self):
        return jsonify({
            "created": True
        })
