#!/usr/bin/env python3
"""a class to manage the API authentication"""

import base64
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string
        base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not type(base64_authorization_header) == str:
            return None
        try:
            valid_Base64 = base64.b64decode(base64_authorization_header.encode(
                'utf-8'))
            return valid_Base64.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from
        the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not type(decoded_base64_authorization_header) == str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user = decoded_base64_authorization_header.split(":")
        return user[0], user[1]
