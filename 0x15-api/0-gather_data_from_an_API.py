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
            emp_name = u_resp.get('name')
            todos = [t for t in t_resp if t.get('userId') == emp_id]
            completed = [t for t in todos if t.get('completed')]
            print('Employee {} is done with tasks({}/{}):'.format(
                        emp_name,
                        len(completed),
                        len(todos)))
            for t in completed:
                print('\t {}'.format(t.get('title')))
