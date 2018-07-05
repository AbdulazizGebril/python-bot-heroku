
# coding: utf-8

# In[1]:


# Dependencies
import os
import tweepy
import time
from datetime import datetime
import json
from config import (CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)

# In[2]:
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

# Twitter API Keys

if 'DYNO' in os.environ:
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']


# In[3]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[4]:


# Create a function that tweets
def TweetOut(minutes):
    api.update_status(
        f"Can't stop. Won't stop. I've been tweeting for {minutes} minutes!")


# In[5]:


#Declare a 'beginning'
then = datetime(2018, 7, 5, 15, 17, 25)


# In[ ]:


# Infinitely loop
while(True):

    # Make something to tweet to avoid duplicates
    now  = datetime.now()
    duration = now - then
    seconds = duration.total_seconds()
    minutes = round(divmod(seconds, 60)[0])

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(minutes)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)
