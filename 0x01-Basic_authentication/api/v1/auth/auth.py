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
        Returns True if the path is not in the list of strings excluded_paths
        """
        if path:
            if path.endswith('/'):
                altr = path[:-1]
            else:
                altr = path + '/'

            if exluded_path and exluded_path != []:
                if path in exluded_path or altr in exluded_path:
                    return False

                for end_fil in exluded_path:
                    cprs = end_fil[:-1]
                    cpath = path[:len(cprs)]
                    if cpath == cprs:
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
