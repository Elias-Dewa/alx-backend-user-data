#!/usr/bin/env python3
"""a class to manage the API authentication"""

from typing import List, TypeVar
from flask import request


class Auth():
    """Defines the authentication mechanism"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        if excluded_paths is None or not len(excluded_paths) or not path:
            return True
        for element in excluded_paths:
            if element.endswith("*"):
                if path.startswith(element[0:1]):
                    return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return None
