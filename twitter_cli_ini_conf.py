#!/usr/bin/python
# coding: utf-8
# author: oleg

import sys
from tweepy import OAuthHandler, API
from ConfigParser import ConfigParser

msg = reduce(lambda x, y: x + " " + y, sys.argv[1:])
c = ConfigParser()
with open(config) as f:
    c.readfp(f)
conf = dict(c.items('twitter'))
auth = OAuthHandler(conf['consumer_key'], conf['consumer_secret'])
auth.set_access_token(conf['access_key'], conf['access_secret'])
API(auth).update_status(msg)
