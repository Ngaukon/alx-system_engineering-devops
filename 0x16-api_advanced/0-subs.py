#!/usr/bin/python3
"""Function to query the number of subscribers for a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers to the subreddit. Returns 0 if the subreddit is not found.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the subreddit exists; if not, return 0
    if response.status_code == 404:
        return 0
    
    # Parse the response to get the subscriber count
    results = response.json().get("data")
    return results.get("subscribers")
