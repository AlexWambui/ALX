#!/usr/bin/python3

""" returns the number of subscribers for a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """returns the no of subscribers on a subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        no_subs = data.get("data").get("subscribers")
        return no_subs
    else:
        return 0