# import code for encoding urls and generating md5 hashes
import urllib3, hashlib
import requests

Class gravatarImage(object):
    def __init__(self, email, size):
        self.email = email
        self.size = size

    def getImage():
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?"
        gravatar_url += 's=' + str(size)

