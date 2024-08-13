#!/usr/bin/python3
"""Function to print the titles of the 10 hottest posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    
    If the subreddit is invalid or not found, the function prints 'None'.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"  # Custom User-Agent to avoid Too Many Requests errors
    }
    params = {
        "limit": 10  # Limit the number of posts retrieved to the top 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    # Check if the subreddit exists; if not, print 'None' and exit the function
    if response.status_code == 404:
        print("None")
        return
    
    # Extract the post data from the JSON response
    results = response.json().get("data")
    
    # Loop through the top 10 posts and print their titles
    [print(c.get("data").get("title")) for c in results.get("children")]
