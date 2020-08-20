import logging
import os
import time
import json
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


def notify(url, diff_text=""):
    # text messages are limited to 160 characters, so use 130 as a safe size
    message = "Changed URL: {}. \n{}".format(url, diff_text[0:100])
    twilio_client.send_message(message,
                               recipient_phone_num=RECIPIENT_PHONE_NUM)
    logging.info(message)


def process_news(db, job_name, sources):
    logging.debug("Processing job {}".format(job_name))

    url = sources[job_name]["url"]
    current_html_doc = requests.get(url)
    if sources[job_name].get("format") == "json":
        current_version = get_json_element(text=current_html_doc.text,
                                           element_selector=sources[job_name]["element_selector"])
    else:
        current_version = get_element_text(html=current_html_doc.text,
                                           element_selector=sources[job_name]["element_selector"])

    if current_version is not None:

        last_version = db.get_last_crawl(news_source=job_name)

        diff_string = get_diff_string(current_version, last_version)
        if last_version != current_version:
            redirect_url = sources[job_name].get("redirect_url") or url
            notify(redirect_url, diff_text=diff_string)

        db.save_last_crawl(job_name, current_version, diff_string=diff_string)


def get_diff_string(current_version, last_version):
    if last_version:
        diff_string = "\n".join(list(unified_diff(last_version.splitlines(), current_version.splitlines())))
    else:
        diff_string = current_version
    return diff_string


def get_element_text(html, element_selector):
    soup = BeautifulSoup(html, 'html.parser')
    current_element_html = soup.find(None, element_selector)
    if current_element_html is not None:
        current_element_html = current_element_html.get_text(strip=True)
    return current_element_html


def get_json_element(text, element_selector=None):
    if text is not None:
        json_dict = json.loads(text)
        if "key_chain" in element_selector:
            key_chain = element_selector["key_chain"]
            element = json_dict
            for key in key_chain:
                element = element.get(key)
                if element is None:
                    break
            json_dict = element

    return json.dumps(json_dict)


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
