#!/usr/bin/python3
"""queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """ recursively query reddit api
    to return list of hot posts
    for a subreddit
    """
    base_url = 'https://www.reddit.com/r/{}/top.json'.format(
            subreddit)
    headers = {
            'User-Agnet':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
            }
    if len(hot_list) == 0:
        #list of hot 
        url = base_url
    else:
        url = base_url + '?after={}_{}'.format(
                hot_list[-1].get('kind'),
                hot_list[-1].get('data').get('id')
                )
    resp = requests.get(url, headers=headers)
    resp2 = json.loads(resp.text)
    try:
        data = resp2.get('data')
        res = data.get('children')
    except:
        return None
    if res is None or data is None or len(res) < 1:
        return hot_list
    hot_list.extend(res)
    return recurse(subreddit, hot_list)
