#!/usr/bin/env python3
"""
Module containing filter_datum function
"""
from typing import List
import re


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """ Returns a log message obfuscated """
    for fl in fields:
        message = re.sub(f'{fl}=.*?{separator}',
                         f'{fl}={redaction}{separator}', message)
    return message
