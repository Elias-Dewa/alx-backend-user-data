#!/usr/bin/env python3
"""_summary_"""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str):
    """Define a method  that returns the log message obfuscated"""
    for field in fields:
        message = re.sub(field + "=.*" + separator,
                         field + "=" + redaction, message)
