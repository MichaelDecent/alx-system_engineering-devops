#!/usr/bin/python3
"""
This Module contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'michaeldecent'}
    params = {'after': after}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code != 200:
        return None

    response_data = response.json()

    for data in response_data['data']['children']:
        hot_list.append(data['data']['title'])

    after = response_data['data']['after']
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
