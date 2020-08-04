from bs4 import BeautifulSoup
import requests
import os
import twilio_client
from config.twilio import RECIPIENT_PHONE_NUM

sources = {
    "treasury_emergency_loans": {
        "url": "https://home.treasury.gov/policy-issues/cares/preserving-jobs-for-american-industry/loans-to-air-carriers-eligible-businesses-and-national-security-businesses",
        "element_selector": "national-loans"
    }
}


def notify(url, element_name):
    print(url, element_name)
    twilio_client.send_message("URL {} had a change in element {}".format(url, element_name),
                               recipient_phone_num=RECIPIENT_PHONE_NUM)


def process_news(job_name, sources):
    url = sources[job_name]["url"]
    element_name = sources[job_name]["element_selector"]
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    current_element_html = soup.find(None, {"id": element_name})
    if current_element_html is not None:
        current_element_html = current_element_html.get_text(strip=True)

        last_load_fn = "diffs/{}.txt".format(job_name)
        if os.path.exists(last_load_fn):
            with open(last_load_fn) as f:
                last_load = f.read().strip()
            if last_load != current_element_html:
                notify(url, element_name)

            if current_element_html != last_load:
                notify(url, element_name)

        with open(last_load_fn, "w") as f:
            f.write(current_element_html)


if __name__ == "__main__":
    os.makedirs("diffs", exist_ok=True)
    process_news("treasury_emergency_loans", sources)
    notify("http://test", "test")
