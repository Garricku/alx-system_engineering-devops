#!/usr/bin/python3
"""This is the 0-subs module"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers (total subscribers) for the subreddit.
        Returns 0 if invalid subreddit.
    """
    platform = "windows10"
    ver = "v1.0"
    id = "alxricku777"
    by = "(by /u/Worth-Programmer7788)"
    try:
        headers = {'User-Agent': f'{platform}:{id}:{ver} {by}'}
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
