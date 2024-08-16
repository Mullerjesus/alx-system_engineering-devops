#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints the titles of the top ten hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Response Code: {response.status_code}")  # Debugging line
        print(f"Response Text: {response.text}")  # Debugging line
        
        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children']:
                print(post['data']['title'])
        elif response.status_code == 404:
            print("Subreddit not found.")
        elif response.status_code == 403:
            print("Access forbidden. Check if the subreddit is private or restricted.")
        else:
            print(f"Received an unexpected status code: {response.status_code}")
    except ValueError as e:
        print("JSONDecodeError:", e)
        print("Response Text: ", response.text)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(f"Top ten posts in r/{subreddit}:")
    top_ten(subreddit)
