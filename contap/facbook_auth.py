# Some code borrowed from here:
# https://github.com/pythonforfacebook/facebook-sdk/blob/master/examples/oauth/facebookoauth.py
import base64
import cgi
import hashlib
import hmac
import logging
import os.path
import time
import urllib3
from cookies import Cookie
import simplejson as json
import requests


FACEBOOK_APP_ID = "your app id"
FACEBOOK_APP_SECRET = "your app secret"

class FacebookOAuth(object):
    """docstring for FacebookOAuth"""
    def __init__(self, arg):
        super(FacebookOAuth, self).__init__()
        self.arg = arg

    def current_user(self):
        """Returns the logged in Facebook user, or None if unconnected."""
        if not hasattr(self, "_current_user"):
            self._current_user = None
            user_id = self.cookies.get("fb_user").value
            if user_id:
                self._current_user = User.get_by_key_name(user_id)
        return self._current_user