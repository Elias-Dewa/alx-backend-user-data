#!/usr/bin/env python3
"""Auth module"""
from typing import Union
from uuid import uuid4
from bcrypt import hashpw, gensalt, checkpw

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ method that takes in a password string arguments and returns bytes"""
    return hashpw(password.encode('utf8'), gensalt())


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
        if checkpw(password.encode(), user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> str:
        """It takes an email string argument and returns
        the session ID as a string"""
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, session_id=uuid)
            return uuid
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """a method that returns the corresponding User or None"""
        if not session_id:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """a method that deletes the corresponding session"""
        if not user_id:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id)
        except NoResultFound:
            return None


def _generate_uuid() -> str:
    """generates a random uuid"""
    return str(uuid4())
