#!/usr/bin/env python3
"""Auth module"""
from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> str:
    """ method that takes in a password string arguments and returns bytes"""
    return hashpw(password.encode('utf8'), gensalt())
