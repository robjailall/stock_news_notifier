import logging
import os

import requests
from bs4 import BeautifulSoup

import twilio_client
from config.news_sources import news_sources
from config.twilio import RECIPIENT_PHONE_NUM

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)


def notify(url):
    logging.info("Notifying of change in {}".format(url))
    twilio_client.send_message("URL {} had a change".format(url),
                               recipient_phone_num=RECIPIENT_PHONE_NUM)


def process_news(job_name, sources):
    logging.debug("Processing job {}".format(job_name))
    url = sources[job_name]["url"]
    html_doc = requests.get(url)

    last_version_fn = "diffs/{}.txt".format(job_name)
    if os.path.exists(last_version_fn):
        with open(last_version_fn) as f:
            last_version = f.read().strip()

    current_version_html = get_element_text(html_doc.text, job_name, sources)

    if current_version_html is not None:
        # compare versions
        if last_version != current_version_html:
            notify(url)

        with open(last_version_fn, "w") as f:
            f.write(current_version_html)


def get_element_text(html_doc, job_name, sources):
    element_selector = sources[job_name]["element_selector"]
    soup = BeautifulSoup(html_doc, 'html.parser')
    current_element_html = soup.find(None, element_selector)
    if current_element_html is not None:
        current_element_html = current_element_html.get_text(strip=True)
    return current_element_html


def process_sources(sources):
    for source in sources:
        process_news(job_name=source, sources=sources)


if __name__ == "__main__":
    os.makedirs("diffs", exist_ok=True)
    process_sources(sources=news_sources)
