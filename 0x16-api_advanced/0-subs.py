#!/usr/bin/python3
# 0-subs.py
""" script to obtain subscribers
    count from a subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """ function to get subscriber count"""
    if subreddit and type(subreddit) is str:
        subscribers = 0
        url = f'https://reddit.com/r/{subreddit}/about.json'
        headers = {'user-agent': 'my-app/0.0.1'}
        req = get(url, headers=headers)
        if req.status_code == 200:
            data = req.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
