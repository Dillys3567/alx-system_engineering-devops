#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit

    Returns 0 for invalid subreddit
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ gets the number of subscribers
    return 0 for invalid subreddit
    ensures there are no redirects
    """
    url = 'https://www.reddit.com/r/'
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    url_all = url + '{}/about.json'.format(subreddit)
    resp = requests.get(url_all, headers=headers)
    resp2 = json.loads(resp.text)

    try:
        data = resp2.get('data')
        subs = data.get('subscribers')
    except:
        return 0
    if subs is None:
        return 0
    return int(subs)

