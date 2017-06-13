import requests
import nltk
import os
import tweepy

# in order to tweet, you'll need app keys
# you can create environment variables in your own env
# using autoenv or by using export statements
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

# add cltk models to path
rel_path = os.path.join('/app/cltk_data/latin/model/latin_models_cltk/')
path = os.path.expanduser(rel_path)

def make_str():
	# create whatever sentences here

def make_tweet(str):
    # get Twitter access
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Authentication failed")

    # tweet the string
    api.update_status(str)
