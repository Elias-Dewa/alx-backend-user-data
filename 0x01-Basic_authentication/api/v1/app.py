#!/usr/bin/env python3
"""Basic Authentication on a simple API"""

from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """a method that handles unauthorized errors"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """a method that handles forbidden errors"""
    return jsonify({"error": "Forbidden"}), 403
