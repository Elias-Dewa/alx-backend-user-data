#!/usr/bin/env python3
"""A basic Flask app"""

from flask import Flask, abort, jsonify, request
from auth import Auth

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "password already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
