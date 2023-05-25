#!/usr/bin/env python3
"""function that expects one string argument name password and
returns a salted, hashed password, which is a byte string"""


import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """returns true if password is valid and false otherwise"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
