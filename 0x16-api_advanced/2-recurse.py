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

    try:
        response = requests.get(
            url.format(subreddit),
            headers=headers,
            params=params,
            allow_redirects=False)
        response_data = response.json()
        for data in response_data['data']['children']:
            hot_list.append(data['data']['title'])

        after = response_data['data']['after']

        if not after:
            return hot_list

        return recurse(subreddit, hot_list, after)
    except Exception as e:
        print(None)


if __name__ == "__main__":
    subreddit_name = "python"
    print(recurse(subreddit_name))
