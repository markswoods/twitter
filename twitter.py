# twitter.py - exercising the twitter API via Python

import requests, json
from twython import Twython

twitter = Twython('TqIZlaldlPFtDNImHqTGKEJvx', 'Yzb1JCJbvFylJAvucMd4zVROa5Gmao6qnJv5XoGdhFzYJCIPqL')

# search for tweets containing the phrase "data science"
for status in twitter.search(q = 'from:realDonaldTrump')['statuses']:
    user = status['user']['screen_name'].encode('utf-8')        
    text = status['text'].encode('utf-8')
    print user, ':', text
    print

# print json.dumps(status, sort_keys=True, indent=4, separators=(',', ': '))
