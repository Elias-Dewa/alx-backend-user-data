#!/usr/bin/env python3
"""Define a class that inherits from SessionExpAuth"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Representation of a session db authentication"""

    def create_session(self, user_id=None):
        """Create a session that creates and stores
        new instance of UserSession and returns the Session ID"""
        if not user_id:
            return None

        session_id = super().create_session(user_id)
        if not session_id:
            return None

        kwargs = {'user_id': user_id, 'session_id': session_id}
        usr_session = UserSession(**kwargs)
        usr_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """return a user id by requesting user session"""
        if not session_id:
            return None

    def destroy_session(self, request=None):
        """that destroys the UserSession based on the Session ID
        from the request cookie"""
        if not request:
            return None
