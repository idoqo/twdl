#!/usr/bin/python

import tweepy
import config
import pprint
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

key = config.twitter['consumer_key']
secret = config.twitter['consumer_secret']

auth = tweepy.OAuthHandler(key, secret);
api = tweepy.API(auth)

status = api.get_status(947444826374639617)

def got_media(json_obj):
    return 'extended_entities' in json_obj

def got_video(entities):
    disp = entities[0]
    if 'video_info' in disp:
        return True
    else:
        return False

def get_video_url(entities):
    disp = entities[0]
    info = disp['video_info']
    preferred_variant = info.variants[-1]
    return preferred_variant

ext_entities = status._json['extended_entities']

if got_video(ext_entities):
    pprint.pprint(get_video_url(ext_entities))
else:
    media_obj = ext_entities['media']
    display_url = media_obj[0]
    media_url = display_url['media_url_https']
    print("Got media url: %s\n", media_url)
    urlretrieve(media_url, 'file.jpg')

