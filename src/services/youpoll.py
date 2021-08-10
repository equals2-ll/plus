from logging import debug, info, warning, error, exception
import requests
import re


class YouPoll():

    def __init__(self):
        self._poll_url = "https://youpoll.me"
        self._poll_post_data = {'address': '',
                                'poll-1[question]': '',
                                'poll-1[option1]': '',
                                'poll-1[option2]': '',
                                'poll-1[min]': '1',
                                'poll-1[max]': '10',
                                'poll-1[voting-system]': '0',
                                'poll-1[approval-validation-type]': '0',
                                'poll-1[approval-validation-value]': '1',
                                'poll-1[rating]': '',
                                'voting-limits-dropdown': '3',
                                'reddit-link-karma': '0',
                                'reddit-comment-karma': '0',
                                'reddit-days-old': '30',
                                'responses-input': ''
                                }

        self._poll_id_re = re.compile('youpoll.me/(\d+)', re.I)

    def create_poll(self, title, **kwargs):
        data = self._poll_post_data
        data['poll-1[question]'] = title

        try:
            resp = requests.post(self._poll_url, data=data, **kwargs)
        except:
            warning("Could not create poll (exception in POST)")
            return None,None

        if resp.ok:
            match = self._poll_id_re.search(resp.url)
            poll_id = match.group(1)
            poll_link = f'https://youpoll.me/{poll_id}/'
            return poll_link, poll_id

        else:
            warning("Could not create poll (resp !OK)")
            return None,None
