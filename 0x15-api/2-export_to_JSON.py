#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress,
using an API.
"""
from sys import argv
import json
import requests

URL = "https://jsonplaceholder.typicode.com"  # The API's URL

if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1].isdecimal() and int(argv[1]) >= 0:
            emp_id = int(argv[1])
            u_resp = requests.get('{}/users/{}'.format(URL, emp_id)).json()
            t_resp = requests.get('{}/todos'.format(URL)).json()
            username = u_resp.get('username')
            todos = [t for t in t_resp if t.get('userId') == emp_id]
            emp_dict, tasklist = {}, []
            for t in todos:
                title = t.get('title')
                t_status = t.get('completed')
                tasklist.append({
                    "task": title,
                    "completed": t_status,
                    "username": username})
            emp_dict[str(emp_id)] = tasklist
            with open("{}.json".format(emp_id), "w") as f:
                json.dump(emp_dict, f)
