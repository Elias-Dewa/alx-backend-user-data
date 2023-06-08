#!/usr/bin/env python3
"""A basic Flask app"""

from flask import Flask, abort, jsonify, redirect, request
from auth import Auth

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue"})