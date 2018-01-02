#!/usr/bin/python

import tweepy
import config
import pprint
import argparse

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

key = config.twitter['consumer_key']
secret = config.twitter['consumer_secret']

auth = tweepy.OAuthHandler(key, secret);
api = tweepy.API(auth)

def get_media_url(tweet_id):
    status = api.get_status(tweet_id)

    ent = status._json['extended_entities']
    #dsp_url = ent[0]
    #info = dsp_url['video_info']
    #variant = info.variants[-1]
    #pprint.pprint(variant)
    media_obj = ent['media']
    variants = media_obj[0]['video_info']['variants']
    #default variant to the last option
    return variants[-1]['url']

def download(url, filename=None):
    if filename is None:
        filename = url.rsplit('/', 1)[-1]
    urlretrieve(url, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--url', dest='url', action='store',
        help='URL of tweet to extract media from'
        )
    args = parser.parse_args()
    if args.url is not None:
        tweet_id = args.url.rsplit('/', 1)[-1]
        url = get_media_url(tweet_id)
        download(url)
    else:
        print("URL parameter is required.")