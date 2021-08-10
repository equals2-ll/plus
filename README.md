# Plus
Mangaplus chapter discussion bot for [/r/manga](https://reddit.com/r/manga/). Still unofficial. T_T
Automate posting newly published chapters to Reddit. 

Currently operates under the account [/u/AutoShonenpon](https://www.reddit.com/user/AutoShonenpon/).

Codebase is largely inspired by [r-anime/holo](https://github.com/r-anime/holo)

## Requirements
* Python 3.8+
* `requests`
* `praw`
* `praw-core`
* `protobuf`
* `ruamel.yaml`
* `schedule`
* `tabulate`
* `Unidecode`
* `urllib3`
* `websocket-client`

### Modules

Name|Command
:--|:--
Update shows|python plus.py -m update
Edit shows|python plus.py -m edit [show-config]
Setup database|python plus.py -m setup

## Quick setup for local development

1. Update config file with your desired useragent and reddit details. You can generate a Reddit OAuth key by [following the steps in the Getting Started section](https://github.com/reddit-archive/reddit/wiki/OAuth2#getting-started) of their GitHub wiki. The subreddit the bot will be posting to, can be changed through python plus.py -s [subreddit] or by changing the config file

```
[reddit]
username = 
password = 
client_id =  
client_secret = 
user_agent= 
subreddit = 
```

2. Set up the database by running `python src/plus.py -m setup`
3. Load the desired manga config files by running `python src/plus.py -m edit mangaplus.yaml`
4. Update the show information by running `python src/plus.py -m update`
5. The bot is now ready to post threads with `python src/plus.py`

## Upcoming features
1. Automate manga popularity chart 
2. Upon multiple requests by users, discord automate posting 