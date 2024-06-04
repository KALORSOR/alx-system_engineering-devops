#!/usr/bin/python3
"""
Using reddit's API
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    # Define the base URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Define the parameters for the API request
    params = {'limit': 100}
    if after:
        params['after'] = after
    
    # Make the API request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response is valid
    if response.status_code != 200:
        return None
    
    try:
        # Parse the response JSON
        data = response.json()
        articles = data['data']['children']
        for article in articles:
            hot_list.append(article['data']['title'])
        
        # Check if there is a next page
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

