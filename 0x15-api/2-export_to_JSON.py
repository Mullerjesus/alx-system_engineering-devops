#!/usr/bin/python3
"""Extend Python script to export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]

    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + f"todos", params={"userId": user_id}).json()

    # Create a list to store tasks information
    tasks_info = []
    for task in todos:
        # Create a dictionary for each task
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"]
        }
        # Append the task dictionary to the tasks list
        tasks_info.append(task_dict)

    # Create a dictionary with the user id as the key and the tasks list as the value
    user_tasks = {user_id: tasks_info}

    # Write the JSON data to a file
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile, indent=4)

    print(f"Data for user {user_id} has been saved to {user_id}.json")
