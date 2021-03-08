# Stock News Notifier

Polls news sources described in `config/news_sources.py`, checks to see if they have changed since the last poll, and uses Twilio to send a push notifiation for the news sources that have changed.

# Running

## Setup and run

1. Setup a Twilio account and add `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_AUTH_TOKEN`, and `TWILIO_FROM_PHONE_NUM` to your environment.
1. (optional) Setup a database a SQL database and set `DATABASE_URL` and `DB_SOURCE_TYPE` in your environment.
1. `python get_news.py`

## Debugging

- Unset `DB_SOURCE_TYPE` to use a local text file as the database rather than postgres. It saves data into the `diffs` folder in the current directory
- Set `DEVELOPMENT_MODE=true` to poll the news sources only once
- Set `LOGLEVEL=debug` to print more stuff
- Set `TWILIO_TESTING=1` to not actually send a push notification

# Example Heroku Setup

    DATABASE_URL=https://mydatabase
    DB_SOURCE_TYPE=postgres
    RECIPIENT_PHONE_NUM="+5555555555"
    TWILIO_ACCOUNT_SID=123
    TWILIO_AUTH_TOKEN=abc
    TWILIO_FROM_PHONE_NUM="+5555555555"
    