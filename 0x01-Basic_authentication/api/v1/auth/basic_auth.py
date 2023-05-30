#!/usr/bin/env python3
"""a class to manage the API authentication"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Defines a BasicAuth class that inherits from Auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication"""
        if authorization_header is None:
            return None
        if not type(authorization_header) == str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        header = authorization_header.split(' ')
        return header[1]
