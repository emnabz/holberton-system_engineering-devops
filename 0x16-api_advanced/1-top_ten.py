#!/usr/bin/python3
""" a function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(
        url,
        headers={"user-Agent": "Custom"},
        params={"limit": 10},
        allow_redirects=False).json()
    try:
        for request in r["data"]["children"]:
            print(request["data"]["title"])
    except KeyError:
        print("None")
