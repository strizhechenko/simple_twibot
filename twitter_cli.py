#!/usr/bin/python

# coding: utf-8
# author: oleg
import sys
import tweepy

msg = ''
sys.argv.remove(sys.argv[0])
for i in sys.argv:
    msg = msg + i + " "
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
tweepy.API(auth).update_status(msg)
