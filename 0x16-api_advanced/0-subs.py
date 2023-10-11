#!/usr/bin/python3
"""
This module contains a  function that queries the
Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API
    and returns the number of subscribers
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(
            url.format(subreddit),
            headers={'User-Agent': 'michaeldecent'},
            allow_redirects=False)
        subreddit_info = response.json()
        return subreddit_info['data']['subscribers']
    except Exception as e:
        return 0


if __name__ == "__main__":
    subreddit_name = "python"
    print(number_of_subscribers(subreddit_name))
