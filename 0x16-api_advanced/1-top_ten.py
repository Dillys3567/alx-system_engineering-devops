#!/usr/bin/python3
"""queries the Reddit API
    prints the titles of the first 10 hot posts 
    listed for a given subreddit
"""
import json
import requests
import sys


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    prints none for an invalid subreddit
    does not allow redirects
    """
    base_url = 'https://www.reddit.com/r/'
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
            }
    url = base_url + '{}/top/.json?count=10'.format(subreddit)
    resp = requests.get(url, headers=headers)
    resp2 = json.loads(resp.text)

    try:
        data = resp2.get('data')
        res = data.get('children')
    except:
        print('None')
    if res is None or data is None or len(res) < 1:
        print('None')

    for i, post_dict in enumerate(res):
        if i == 10:
            break
        print(post_dict.get('data').get('title'))
