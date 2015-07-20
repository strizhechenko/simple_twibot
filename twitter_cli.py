#!/usr/bin/python
# coding: utf-8
# author: oleg

import sys, tweepy

msg = reduce(lambda x, y: x + " " + y, sys.argv[1:])
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
tweepy.API(auth).update_status(msg)
