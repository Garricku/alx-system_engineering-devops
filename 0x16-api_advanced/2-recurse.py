#!/usr/bin.python3
"""This is the 1-top_ten module"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of hot article titles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store hot article titles (initially empty).
        after (str): Token for pagination (initially None).

    Returns:
        list: List of hot article titles or None if invalid subreddit.
    """
    platform = "windows10"
    ver = "v1.0"
    id = "alxricku777"
    by = "(by /u/Worth-Programmer7788)"
    try:
        headers = {'User-Agent': f'{platform}:{id}:{ver} {by}'}
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
        params = {'after': after} if after else {}
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        print(f"{e}")
        return None
