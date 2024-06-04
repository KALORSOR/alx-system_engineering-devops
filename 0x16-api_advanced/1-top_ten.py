#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
from requests import get
import requests

def top_ten(subreddit):
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    
    if response.status_code != 200:
        print(None)
        return

    try:
        
        data = response.json()
        articles = data['data']['children']

        
        if not articles:
            print(None)
            return

        
        for article in articles:
            print(article['data']['title'])

    except ValueError:
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 0-main.py <subreddit>")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)

