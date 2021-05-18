#!/usr/bin/python3
'''
a function that queries the Reddit API
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = {'User-agent': 'greg'}
    sub = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=user_agent)

    try:
        sub = sub.json().get('data')
        after = sub.get('after')
        sub = sub.get('children')
        for obj in sub:
            hot_list.append(obj['data'].get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except BaseException:
        return(None)
