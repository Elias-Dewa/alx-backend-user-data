#!/usr/bin/env python3
"""Error handler endpoint"""

from flask import Flask, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'])
def unauthorized() -> str:
    """the error handler for 401"""
    abort(401)


@app_views.route('/forbidden', methods=['GET'])
def forbidden() -> str:
    """the error handler for 403"""
    abort(403)
