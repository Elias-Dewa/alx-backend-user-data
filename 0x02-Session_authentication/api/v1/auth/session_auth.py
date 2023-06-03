#!/usr/bin/env python3
"""Define a class SessionAuth that inherits from Auth"""
from models.user import User
from uuid import uuid4
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Represents a session authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """a method to creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """a method that returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """a method that returns a User instance based on a cookie value"""
        cookie = self.session_cookie(request)
        if cookie is None:
            return None
        usr_id = self.user_id_for_session_id(cookie)
        return User.get(usr_id)

    def destroy_session(self, request=None):
        """method that deletes the user session / logout"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        usr_id = self.user_id_for_session_id(session_id)
        if not session_id or not usr_id:
            return False
        del self.user_id_for_session_id[session_id]
        return True
