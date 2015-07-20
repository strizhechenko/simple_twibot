#!/usr/bin/python
# coding: utf-8
# author: oleg

import sys
from tweepy import OAuthHandler, API

msg = reduce(lambda x, y: x + " " + y, sys.argv[1:])
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
API(auth).update_status(msg)
