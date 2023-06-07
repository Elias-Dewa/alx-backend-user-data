#!/usr/bin/env python3
"""Auth module"""

from uuid import uuid4
import bcrypt

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """a method that registers a user with the authentication"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """returns boolean indicating whether the user is valid"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if bcrypt.checkpw(password.encode(), user.hashed_password):
            return True
        return False


def _generate_uuid():
    """generates a random uuid"""
    return str(uuid4())


def _hash_password(password: str) -> str:
    """ method that takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
