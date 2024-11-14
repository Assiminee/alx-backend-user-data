#!/usr/bin/env python3
"""
basic_auth module
Contains BasicAuth class
"""
import base64
from email.charset import BASE64
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value
        """
        db64ah = decoded_base64_authorization_header
        if db64ah and type(db64ah) is str and ":" in db64ah:
            email, password = db64ah.split(":")
            return email, password

        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password
        """
        email = user_email
        pwd = user_pwd
        if email and pwd and type(email) is str and type(pwd) is str:
            try:
                user = User.search({'email': email})
                if user and user != []:
                    for user in user:
                        if user.is_valid_password(pwd):
                            return user
            except Exception:
                return None

        return None
