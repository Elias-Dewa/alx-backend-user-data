#!/usr/bin/env python3
"""Flask view that handles all routes for the Session authentication"""

from os import getenv
from models.user import User
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'])
def login() -> str:
    """method to handles login routes for the Session authentication"""
    usr_email = request.form.get('email')
    usr_password = request.form.get('password')
    if not usr_email:
        return jsonify({"error": "email missing"}), 400
    if not usr_password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": usr_email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(usr_password):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        session_name = getenv('SESSION_NAME')
        usr_json = jsonify(user.to_json())
        usr_json.set_cookie(session_name, session_id)
        return usr_json
