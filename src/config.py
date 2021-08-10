import configparser
from logging import warning
import os


class WhitespaceFriendlyConfigParser(configparser.ConfigParser):
    def get(self, section, option, *args, **kwargs):
        val = super().get(section, option, *args, **kwargs)
        return val.strip('"')


class Config:
    def __init__(self):
        self.debug = False
        self.module = None
        self.database = None

        self.reddit_username = None
        self.reddit_password = None
        self.reddit_client_id = None
        self.reddit_client_secret = None
        self.reddit_user_agent = None
        self.subreddit=None

        self.post_title = None
        self.comment_body = None


def from_file(file_path):
    parsed = WhitespaceFriendlyConfigParser()
    success = parsed.read(file_path)
    if len(success) == 0:
        warning("Failed to load config file")
        return None

    config = Config()

    if "data" in parsed:
        sec = parsed["data"]
        config.database = sec.get("database", None)

    if "reddit" in parsed:
        sec = parsed["reddit"]
        config.reddit_username = sec.get("username", None)
        config.reddit_password = sec.get("password", None)
        config.reddit_client_id = sec.get("client_id", None)
        config.reddit_client_secret = sec.get("client_secret", None)
        config.reddit_user_agent = sec.get("user_agent", None)
        config.subreddit=sec.get("subreddit",None)

    if "post" in parsed:
        sec = parsed["post"]
        config.post_title = sec.get("title", None)
        config.comment_body = sec.get("comment", None)

    return config


def validate_config(config):
    def is_bad_str(s):
        return s is None or len(s) == 0

    if is_bad_str(config.database):
        return "database missing"
    if is_bad_str(config.reddit_username):
        return "reddit username missing"
    if is_bad_str(config.reddit_password):
        return "reddit password missing"
    if is_bad_str(config.reddit_client_id):
        return "reddit cliet id missing"
    if is_bad_str(config.reddit_client_secret):
        return "reddit client secret missing"
    if is_bad_str(config.reddit_user_agent):
        return "reddit user agent missing"
    if is_bad_str(config.post_title):
        return "post title missing"
    if is_bad_str(config.comment_body):
        return "comment body missing"
