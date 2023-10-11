#!/usr/bin/python3
"""
This Module contains a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.
    """
    url = f'https://www.reddit.com//r/{subreddit}/top.json'
    response = requests.get(
        url.format(subreddit),
        headers={'User-Agent': 'michaeldecent'},
        allow_redirects=False)

    try:
        response_data = response.json()
        for count, data in enumerate(response_data['data']['children']):
            print(data['data']['title'])
            if count == 9:
                break
    except Exception as e:
        print(None)


if __name__ == "__main__":
    subreddit_name = "python"
    top_ten(subreddit_name)
