
# coding: utf-8

# In[ ]:


# Dependencies
import os
import tweepy
import time
from datetime import datetime
import json
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)


# In[ ]:


# Twitter API Keys
try:
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
except:
    consumer_key = consumer_key
    consumer_secret = consumer_secret
    access_token = access_token 
    access_token_secret = access_token_secret


# In[ ]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[ ]:


# Create a function that tweets
def TweetOut(minutes):
    api.update_status(
        f"Can't stop. Won't stop. I've been tweeting for {minutes} minutes!")


# In[ ]:


# Make something to tweet to avoid duplicates

then = datetime(2018, 7, 5, 15, 17, 25)        
now  = datetime.now() 
duration = now - then                         
seconds = duration.total_seconds()
minutes = round(divmod(seconds, 60)[0])


# In[ ]:


# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(minutes)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

