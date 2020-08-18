import logging
import os
import time
from difflib import unified_diff

import requests
from bs4 import BeautifulSoup

import twilio_client
from config.news_sources import news_sources
from config.notifier import CHECK_INTERVAL_SECONDS, DEVELOPMENT_MODE, DB_SOURCE_TYPE
from config.twilio import RECIPIENT_PHONE_NUM

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)


def get_db(source_type):
    if source_type == "postgres":
        from dbs.postgres_db import create_db
        return create_db()
    else:
        from dbs.file_db import create_db
        return create_db()


def notify(url):
    logging.info("Notifying of change in {}".format(url))
    twilio_client.send_message("URL {} had a change".format(url),
                               recipient_phone_num=RECIPIENT_PHONE_NUM)


def process_news(db, job_name, sources):
    logging.debug("Processing job {}".format(job_name))

    url = sources[job_name]["url"]
    current_html_doc = requests.get(url)
    current_version = get_element_text(html=current_html_doc.text,
                                       element_selector=sources[job_name]["element_selector"])

    if current_version is not None:

        last_version = db.get_last_crawl(news_source=job_name)
        if last_version:
            diff_string = "\n".join(list(unified_diff(last_version.splitlines(), current_version.splitlines())))
        else:
            diff_string = current_version

        if last_version != current_version:
            notify(url)

        db.save_last_crawl(job_name, current_version, diff_string=diff_string)


def get_element_text(html, element_selector):
    soup = BeautifulSoup(html, 'html.parser')
    current_element_html = soup.find(None, element_selector)
    if current_element_html is not None:
        current_element_html = current_element_html.get_text(strip=True)
    return current_element_html


def process_sources(sources):
    db = get_db(source_type=DB_SOURCE_TYPE)
    for source in sources:
        process_news(db=db, job_name=source, sources=sources)


if __name__ == "__main__":
    while True:
        process_sources(sources=news_sources)

        # don't continue this loop in dev mode
        if DEVELOPMENT_MODE:
            break
        time.sleep(CHECK_INTERVAL_SECONDS)
