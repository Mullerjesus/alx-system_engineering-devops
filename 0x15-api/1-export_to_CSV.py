#!/usr/bin/python3
"""Returns Todo list for a given employee id
and exports data in the CSV format"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    id = argv[1]

    user = requests.get(url + f"users/{id}").json()
    todos = requests.get(url + f"todos", params={"userId": id}).json()

    file = f"{id}.csv"
    with open(file, "w") as f:
        for item in todos:
            # Split the long line into multiple lines
            f.write(f'"{id}","{user["username"]}","{item["completed"]}","'
                    f'{item["title"]}"\n')
