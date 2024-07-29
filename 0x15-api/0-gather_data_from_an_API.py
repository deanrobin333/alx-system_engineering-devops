#!/usr/bin/python3
# 0-gather_data_from_an_API.py

'''script that, using this REST API - https://jsonplaceholder.typicode.com/
, for a given employee ID, returns information about his/her
TODO list progress
'''

import json
import requests
from sys import argv

web_url = 'https://jsonplaceholder.typicode.com'


def run_api():
    '''Gets information about an employee'''
    user_id = argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(web_url, user_id)
    # print("user url is: {}".format(user_url))

    # get info from api
    response = requests.get(user_url)
    # pull data from api
    data = response.text
    # parse the data into JSON format
    data = json.loads(data)
    # extract user data, in this case, name of employee
    name = data[0].get('name')
    # print("id is: {}".format(user_id))
    # print("name is: {}".format(name))

    # get user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # print("tasks url is: {}".format(tasks_url))

    # get info from api
    response = requests.get(tasks_url)
    # pull data from api
    tasks = response.text
    # parse the data into JSON format
    tasks = json.loads(tasks)

    # initialize completed count as 0 and find total number of tasks
    completed = 0
    total_tasks = len(tasks)

    # initialize empty list for completed tasks
    completed_tasks = []
    # loop through tasks counting number of completed tasks
    for task in tasks:

        if task.get('completed'):
            # print("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # print the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == ('__main__'):
    run_api()
