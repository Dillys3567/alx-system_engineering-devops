#!/usr/bin/python3
"""queries the Reddit API
    parses the title of all hot articles
    and prints a sorted count of given keywords
"""
import json
import requests
import sys


def count_words(subreddit, word_list):
