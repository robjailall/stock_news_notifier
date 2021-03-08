# Running

## Setup and run

1. Setup a database a SQL database and set `DATABASE_URL` and `DB_SOURCE_TYPE` in your environment.
1. Setup a Twilio account and add `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_AUTH_TOKEN`, and `TWILIO_FROM_PHONE_NUM` to your environment.
1. `python get_news.py`

## Debugging

1. Set `DEVELOPMENT_MODE=true` to poll the news sources only once
1. Set `LOGLEVEL=debug` to print more stuff
1. Set `TWILIO_TESTING=1` to not actually send a push notification

# Example Heroku Setup

    DATABASE_URL=
    DB_SOURCE_TYPE=postgres
    RECIPIENT_PHONE_NUM="+5555555555"
    TWILIO_ACCOUNT_SID=123
    TWILIO_AUTH_TOKEN=abc
    TWILIO_FROM_PHONE_NUM="+5555555555"
    