#!/usr/bin/python3
"""This module queries the Reddit API"""
import requests


def count_words_helper(word: str, text: str) -> int:
    """
    Count the number of occurrences of a word in a string.
    """
    return text.lower().split().count(word.lower())


def count_words(subreddit, word_list, count_dict=None, after=None):
    """
    Recursively count the number of occurrences of keywords in the titles
    of hot articles in a subreddit.
    """

    if count_dict is None:
        count_dict = {}
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title']
        for word in word_list:
            count_dict[word] = count_dict.get(
                word, 0) + count_words_helper(word, title)
        count_dict = count_words(subreddit, word_list,
                                 count_dict, data['data']['after'])

    if after is None and count_dict is not None:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print('{}: {}'.format(word.lower(), count))
