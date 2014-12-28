# coding: utf-8
# author: oleg
import tweepy, threading, sys
from time import localtime, strftime, sleep

replyed = ['']
update_time = 60

def init():
    global api
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


class TwiBot(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def tweet(self, twit):
        if len(twit) <= 140 and len(twit) > 0:
            try:
                api.update_status(twit)
                return True
            except tweepy.TweepError:
                print 'Duplicate'
        return False

line = ''
sys.argv.remove(sys.argv[0])
for i in sys.argv:
    line = line + i + " "

init()
s = TwiBot()
s.tweet(line)
