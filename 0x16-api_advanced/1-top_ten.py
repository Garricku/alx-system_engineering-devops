#!/usr/bin/python3
"""This is the 1-top_ten module"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for
    a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    platform = "windows10"
    ver = "v1.0"
    id = "alxricku777"
    by = "(by /u/Worth-Programmer7788)"
    try:
        headers = {'User-Agent': f'{platform}:{id}:{ver} {by}'}
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    except Exception as e:
        print("None")
