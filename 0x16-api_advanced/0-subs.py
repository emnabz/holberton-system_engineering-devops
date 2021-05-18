#!/usr/bin/python3
""" a function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={"User-agent": "Custom"},
                     allow_redirects=False).json()
    try:
        return r["data"]["subscribers"]
    except KeyError:
        return 0
