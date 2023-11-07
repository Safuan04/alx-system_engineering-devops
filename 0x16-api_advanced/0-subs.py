#!/usr/bin/python3
"""Importing necessary modules"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'MyAPI'}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 200:
        Data = req.json()
        number_of_subs = Data['data']['subscribers']
        return number_of_subs
    else:
        return 0
