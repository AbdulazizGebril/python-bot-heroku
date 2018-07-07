# Python Bot Heroku Deployment

Fork and/or clone this repo.

## Using Environment Variables

Create a `config.py` file and add your Twitter creds, like so:
```
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
```

On Heroku, under Settings, click `Reveal Config Vars` and add...
```
CONSUMER_KEY
CONSUMER_SECRET
ACCESS_TOKEN
ACCESS_TOKEN_SECRET
```
...with their corresponding values.

## Deploy
