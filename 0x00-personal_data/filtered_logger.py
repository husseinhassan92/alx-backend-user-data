#!/usr/bin/env python3
"""
Script for handling Personal Data
"""

from typing import List
import re
import logging
from os import environ
import mysql.connector


# # PII fields to be redacted
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Replaces sensitive information in a message with a redacted value
    based on the list of fields to redact
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
