# Python Bot Heroku Deployment

Fork and/or clone this repo.

## Using Environment Variables

Create a `config.py` file and add your Twitter creds, like so:
```
consumer_key = "pWaFRDgs0S7kyzHX9ZLfNwxhX"
consumer_secret = "iAcooaCTfBUi9HpZM2ZpDAwKyNdRnQX3Ed9nOcb4mWJELgqlGH"
access_token = "777278389-wVm7P0RGRNr4YHVW85zXz8u4ngMs3EBaiKijmdBV"
access_token_secret = "y1o6ddNxbJfHz2h3mOux10LKDbLbFAvQ0VBTy4Fovp4Hs"
```

On Heroku, under Settings, click `Reveal Config Vars` and add...
```
ACCESS_TOKEN
ACCESS_TOKEN_SECRET
CONSUMER_KEY
CONSUMER_SECRET
```
...with their corresponding values.

## Deploy
