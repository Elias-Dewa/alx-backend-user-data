#!/usr/bin/env python3
"""A basic Flask app"""

from flask import Flask, abort, jsonify, redirect, request
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form('email')
    password = request.form('password')
    if AUTH.valid_login(email, password) is False:
        abort(401)
    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie('session_id', session_id)
    return res


@app.route('/sessions', methods=['DELETE'])
def logout():
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user or not session_id:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user or not session_id:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def reset_password_token():
    email = request.form.get('email')
    reset_token = AUTH.get_reset_password_token(email)

    try:
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    password = request.form.get('password')

    try:
        AUTH.update_password(reset_token, password)
    except Exception:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
