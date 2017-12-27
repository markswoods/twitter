#!/usr/bin/env python

from twython import TwythonStreamer
import os
import json
#import ConfigParser

#CONSUMER_KEY = os.environ['CONSUMER_KEY']
#CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
#ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
#ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

#config = ConfigParser.ConfigParser()
#config.read('config.ini')

with open('config.json', 'r') as f:
    config = json.load(f)

CONSUMER_KEY = config['DEFAULT']['CONSUMER_KEY']
CONSUMER_SECRET = config['DEFAULT']['CONSUMER_SECRET']
ACCESS_TOKEN = config['DEFAULT']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['DEFAULT']['ACCESS_TOKEN_SECRET']

# appending data to a global var is pretty poor form
# but it makes the example much simpler
tweets = []

class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies how to interact with the stream"""
    
    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python dict representing a tweet"""
        
        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)
            print "received tweet #", len(tweets)
            
        # stop when we've collected enough
        if len(tweets) >= 1000:
            self.disconnect()
            
    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()
        
stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# starts consuming public statuses that contain the keyword 'data'
stream.statuses.filter(track='data')

# to consume a sample of all public status, use this
# stream.statuses.sample()

top_hastags = Counter(hashtag['text'].lower()
                for tweet in tweets
                for hashtag in tweet["entities"]["hashtags"])
                
print top_hashtags.most_common(5)