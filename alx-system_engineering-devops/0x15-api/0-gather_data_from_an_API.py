#!/usr/bin/python3
""" Fetches JSON data from an API """

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("name")
    user_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todos = user_todos.json()
    total_todos = 0
    complete_titles = []
    complete_tasks = 0

    for item in user_todos:
        if item.get("userId") == int(user_id):
            total_todos += 1
            if item.get("completed") is True:
                complete_tasks += 1
                complete_titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, complete_tasks, total_todos))
    for title in complete_titles:
        print("\t {}".format(title))
