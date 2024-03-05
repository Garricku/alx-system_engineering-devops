#!/usr/bin/python3
""" this is the 100-count module"""

import requests
from collections import Counter

def count_words(subreddit, word_list, after=None):
    """
    Recursively queries the Reddit API, parses hot article titles, and prints keyword counts.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords (case-insensitive).
        after (str): Token for pagination (initially None).

    Returns:
        None
    """
    try:
        platform = "windows10"
        ver = "v1.0"
        id = "alxricku777"
        by = "(by /u/Worth-Programmer7788)"
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
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        word_list.remove(word)
                        break

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after)
            else:
                word_counts = Counter(word_list)
                sorted_counts = sorted(word_counts.items(),
                                       key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            pass
    except Exception as e:
        print(f"Error fetching data: {e}")
