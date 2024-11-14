#!/usr/bin/env python3
"""
Authentication module
"""
from typing import List, TypeVar, re

from flask import request


class Auth:
    """
    Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if the path is not in the list of strings excluded_paths
        """
        if path and not path.endswith('/'):
            path += '/'

        if (
            not path or
            not excluded_paths or
            len(excluded_paths) == 0
        ):
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                pattern = excluded_path[:-1] + '.*'
                if re.match(pattern, path):
                    return False
            else:
                if excluded_path == path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Validates all requests to secure the API
        """
        if (
            not request or
            not request.headers.get('Authorization')
        ):
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None for now
        """
        return None
