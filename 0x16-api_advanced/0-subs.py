#!/usr/bin/python3  
import requests  

def number_of_subscribers(subreddit):  
    """Queries the Reddit API and returns the number of subscribers to the subreddit."""  
    url = f"https://www.reddit.com/r/{subreddit}/about.json"  
    headers = {"User-Agent": "My-User-Agent"}  
    
    response = requests.get(url, headers=headers, allow_redirects=False)  

    if response.status_code != 200:  
        return 0  

    data = response.json().get("data")  
    if data:  
        return data.get("subscribers", 0)  

    return 0
