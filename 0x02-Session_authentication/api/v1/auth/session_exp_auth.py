#!/usr/bin/env python3
"""Define a class SessionExpAuth that inherits from SessionAuth"""
from datetime import datetime, timedelta
from os import getenv
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Represents  a class expiration session"""

    def __init__(self):
        """Initialize a session"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a session"""
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        session_dict = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return the session id associated"""
        if not session_id:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if not session_dict:
            return None

        user_id = session_dict.get('user_id')
        if not user_id:
            return None

        if self.session_duration <= 0:
            return user_id

        created_time = session_dict.get('created_at')
        if not created_time:
            return None

        if datetime.now() > created_time + timedelta(
                seconds=self.session_duration):
            return None
        return user_id
