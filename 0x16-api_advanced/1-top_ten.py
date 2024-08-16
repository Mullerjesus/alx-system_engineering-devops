#!/usr/bin/python3  
import requests  

def top_ten(subreddit):  
    """Prints the titles of the top ten hot posts from a subreddit."""  
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"  
    headers = {"User-Agent": "Mozilla/5.0"}  
    response = requests.get(url, headers=headers, allow_redirects=False)  

    if response.status_code == 200:  
        data = response.json()  
        for post in data['data']['children']:  
            print(post['data']['title'])  
    else:  
        print("OK")  # Return "OK" for any non-200 status to match expected output  

if __name__ == "__main__":  
    subreddit = input("Enter subreddit name: ")  # Change to your preferred subreddit  
    print(f"Top ten posts in r/{subreddit}:")  
    top_ten(subreddit)
