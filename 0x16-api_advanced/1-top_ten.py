#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "limit": 10
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the response is successful
        if response.status_code != 200:
            print("None")
            return
        
        # Try to parse the JSON response
        results = response.json().get("data")
        if results is None:
            print("None")
            return
        
        # Print the titles of the hot posts
        [print(c.get("data").get("title")) for c in results.get("children")]
        
    except Exception as e:
        # Catch any other unexpected errors
        print("None")
