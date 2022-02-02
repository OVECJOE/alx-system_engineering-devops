#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress,
using an API.
"""
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com"  # The API's URL

if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1].isdecimal() and int(argv[1]) >= 0:
            emp_id = int(argv[1])
            u_resp = requests.get('{}/users/{}'.format(URL, emp_id)).json()
            t_resp = requests.get('{}/todos'.format(URL)).json()
            username = u_resp.get('username')
            todos = [t for t in t_resp if t.get('userId') == emp_id]
            with open('{}.csv'.format(emp_id), "w") as f:
                for t in todos:
                    t_status = t.get('completed')
                    title = t.get('title')
                    f.write('"{}","{}","{}","{}"\n'.format(
                        emp_id, username, t_status, title))
