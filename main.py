
# coding: utf-8

# In[1]:


# Dependencies
import os
import tweepy
import time
import json
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)


# In[2]:


# Twitter API Keys
# if 'CONSUMER_KEY' in os.environ:
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
def TweetOut(tweet_number):
    api.update_status(
        f"Can't stop. Won't stop. Chatting! This is Tweet #{tweet_number}!")


# In[5]:


# Create a function that calls the TweetOut function every minute
counter = 0


# In[6]:


# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1

