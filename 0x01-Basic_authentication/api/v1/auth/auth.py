#!/usr/bin/env python3
"""
Authentication module
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """
    Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns False for now
        """
        if not path.endswith('/'): path += '/'
        if (
            not path or
            not excluded_paths or
            len(excluded_paths) == 0 or
            path not in excluded_paths
        ):
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None for now
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None for now
        """
        return None
