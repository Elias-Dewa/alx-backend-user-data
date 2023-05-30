#!/usr/bin/env python3
"""a class to manage the API authentication"""

from models.user import User
import base64
from typing import TypeVar
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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or not type(user_email) == str:
            return None
        if user_pwd is None or not type(user_pwd) == str:
            return None
        users = User.search({"email": user_email})
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
