#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    subreddit = "programming"  # Change to your preferred subreddit
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers in r/{subreddit}: {subscribers}")
