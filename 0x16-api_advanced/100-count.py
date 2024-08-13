#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
   This module includes functions to count the occurrences of words in 
   Reddit post titles from a specific subreddit.
'''
import requests


def sort_histogram(histogram={}):
    '''Sorts and prints the given histogram.
    
    The histogram is a list of tuples where each tuple contains a word 
    and the count of its occurrences. The function first consolidates 
    duplicate words by summing their counts, then sorts the histogram:
    
    1. Alphabetically by the word (if counts are the same).
    2. In descending order by the count of occurrences.
    
    Args:
        histogram (list of tuples): A list of tuples where each tuple 
        contains a word and its occurrence count.

    Returns:
        None
    '''
    # Filter out words with a count of zero
    histogram = list(filter(lambda kv: kv[1], histogram))
    
    # Consolidate the histogram by summing counts for duplicate words
    histogram_dict = {}
    for item in histogram:
        if item[0] in histogram_dict:
            histogram_dict[item[0]] += item[1]
        else:
            histogram_dict[item[0]] = item[1]
    
    # Convert the consolidated dictionary back into a list of tuples
    histogram = list(histogram_dict.items())
    
    # Sort alphabetically by the word
    histogram.sort(
        key=lambda kv: kv[0],
        reverse=False
    )
    
    # Sort in descending order by the count of occurrences
    histogram.sort(
        key=lambda kv: kv[1],
        reverse=True
    )
    
    # Convert the sorted histogram to a formatted string and print it
    res_str = '\n'.join(list(map(
        lambda kv: '{}: {}'.format(kv[0], kv[1]),
        histogram
    )))
    if res_str:
        print(res_str)


def count_words(subreddit, word_list, histogram=[], n=0, after=None):
    '''Counts the number of times each word in a given word list
    occurs in the titles of the hot posts in a given subreddit.
    
    This function recursively queries the Reddit API to retrieve 
    hot posts from the specified subreddit and counts the occurrences 
    of each word in the word list. The results are accumulated in 
    a histogram and sorted before being printed.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list of str): A list of words to count in the post titles.
        histogram (list of tuples): A list to store the word counts (word, count).
        n (int): The number of posts processed so far.
        after (str): The ID of the last post retrieved, used for pagination.

    Returns:
        None
    '''
    # Headers to mimic a browser request and avoid being blocked by Reddit
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    
    # Define parameters for the API request
    sort = 'hot'
    limit = 30
    
    # Make the request to Reddit API
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            'https://www.reddit.com',
            subreddit,
            sort,
            limit,
            n,
            after if after else ''
        ),
        headers=api_headers,
        allow_redirects=False
    )
    
    # Initialize histogram with the words from word_list if not already initialized
    if not histogram:
        word_list = list(map(lambda word: word.lower(), word_list))
        histogram = list(map(lambda word: (word, 0), word_list))
    
    # Process the response if the request was successful
    if res.status_code == 200:
        data = res.json()['data']  # Extract the JSON data
        posts = data['children']  # Get the list of posts
        titles = list(map(lambda post: post['data']['title'], posts))  # Extract titles
        
        # Update the histogram with word counts from the titles
        histogram = list(map(
            lambda kv: (kv[0], kv[1] + sum(list(map(
                lambda txt: txt.lower().split().count(kv[0]),
                titles
            )))),
            histogram
        ))
        
        # If more posts are available, continue fetching them recursively
        if len(posts) >= limit and data['after']:
            count_words(
                subreddit,
                word_list,
                histogram,
                n + len(posts),
                data['after']
            )
        else:
            # All posts have been processed; sort and print the histogram
            sort_histogram(histogram)
    else:
        # If the request was unsuccessful, return without printing anything
        return
