#!/usr/bin/env python3
"""Define a class that inherits from Base"""
from models.base import Base


class UserSession(Base):
    """Representation of a user session"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize a user session"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
