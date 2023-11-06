#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json


def findmax(input_list):
    return max(input_list)


file_names = ['task01a.txt', 'task01b.txt', 'task01c.txt']
for file_name in file_names:
    with open(file_name, 'r') as file:
        data = json.load(file)

        largest=findmax(data)
        taskname=file_name.split('.')[0]
        print(f"Largest number in {taskname} is : {largest}")
        
