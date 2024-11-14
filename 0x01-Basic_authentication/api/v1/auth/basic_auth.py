#!/usr/bin/env python3
"""
basic_auth module
Contains BasicAuth class
"""
import base64
from email.charset import BASE64

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the
        Authorization header for a Basic Authentication
        """
        if (
            not authorization_header or
            type(authorization_header) != str or
            not authorization_header.startswith('Basic ')
        ):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
    ) -> str:
        """
        Returns the decoded value of a Base64
        string base64_authorization_header
        """
        ah64 = base64_authorization_header
        if ah64 and type(ah64) is str:
            try:
                decoded = base64.b64decode(ah64)
                return decoded.decode('utf-8')
            except (ValueError, TypeError):
                return None

        return None
