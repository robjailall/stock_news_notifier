import os


class FileSource(object):
    def __init__(self):
        os.makedirs("diffs", exist_ok=True)

    def get_last_crawl(self, news_source):
        last_version_fn = "diffs/{}.txt".format(news_source)
        last_version = None
        if os.path.exists(last_version_fn):
            with open(last_version_fn) as f:
                last_version = f.read().strip()
        return last_version

    def save_last_crawl(self, news_source, text, diff_string=""):
        text = text or ""
        fn = "diffs/{}.txt".format(news_source)
        with open(fn, "w") as f:
            f.write(text)


def create_db():
    return FileSource()
