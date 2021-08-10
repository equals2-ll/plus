from logging import debug, info, error, exception
import praw

_r = None
_config = None

def init_reddit(config):
	global _config
	_config = config

def _connect_reddit():
	if _config is None:
		error("Can't connect to reddit without a config")
		return None
	
	return praw.Reddit(client_id=_config.reddit_client_id, client_secret=_config.reddit_client_secret,
					username=_config.reddit_username, password=_config.reddit_password,
					user_agent=_config.reddit_user_agent,
					check_for_updates=False)

def _ensure_connection():
	global _r
	if _r is None:
		_r = _connect_reddit()
	return _r is not None

def submit_link_post(title,url,subreddit):
    _ensure_connection()
    try:
        info(f"Submitting post '{title}'    {url}")
        submission=_r.subreddit(subreddit).submit(title,url=url)
        return submission
    except:
        exception("Failed to submit post")
        return None

def comment_post(submission,comment_text):
    try:
        comment=submission.reply(comment_text)
        return comment
    except:
        exception("Failed to comment post")