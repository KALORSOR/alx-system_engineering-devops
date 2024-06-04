#!/usr/bin/python3
"""
Using reddit's API
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    
    params = {'limit': 100}
    if after:
        params['after'] = after
    
     
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    
    if response.status_code != 200:
        return None
    
    try:
        
        data = response.json()
        articles = data['data']['children']
        for article in articles:
            hot_list.append(article['data']['title'])
        
        
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    
    except ValueError:
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 0-main.py <subreddit>")
    else:
        subreddit = sys.argv[1]
        hot_titles = recurse(subreddit)
        if hot_titles:
            print(hot_titles)
        else:
            print(None)

