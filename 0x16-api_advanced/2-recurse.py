#!/usr/bin/python3
"""Importing necessary modules"""
import requests


def recurse(subreddit, after_link="", hot_list=[]):
    """Returns a list containing the titles of
    all hot articles for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPI'}

    params = {
        'after': after_link,
        'limit': 100
    }

    req = requests.get(url, headers=headers,
                       params=params,
                       allow_redirects=False)

    if req.status_code == 200:
        hotData = req.json()
        hotDataPosts = hotData['data']['children']
        for post in hotDataPosts:
            hot_list.append(post['data']['title'])

        if hotData['data']['after'] is not None:
            after = hotData['data']['after']
            return(recurse(subreddit, after, hot_list))
    else:
        return None

    return hot_list
