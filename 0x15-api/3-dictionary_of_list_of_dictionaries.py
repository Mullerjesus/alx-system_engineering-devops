#!/usr/bin/python3
"""Extend Python script to export data in the JSON format for all employees"""
import json
import requests

def export_all_employees_tasks(url):
    # Get all users
    users = requests.get(url + "users").json()
    # Initialize a dictionary to hold all employees' tasks
    all_employees_tasks = {}

    # Loop through each user
    for user in users:
        user_id = str(user['id'])
        # Get tasks for the current user
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        # Create a list to store tasks information
        user_tasks = []
        for task in todos:
            # Create a dictionary for each task
            task_dict = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            # Append the task dictionary to the user's tasks list
            user_tasks.append(task_dict)
        # Add the user's tasks to the all employees' tasks dictionary
        all_employees_tasks[user_id] = user_tasks

    # Write the JSON data to a file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employees_tasks, jsonfile, indent=4)

    print("Data for all employees has been saved to todo_all_employees.json")

# Set the URL for the API
api_url = "https://jsonplaceholder.typicode.com/"
# Call the function to export all employees' tasks
export_all_employees_tasks(api_url)
