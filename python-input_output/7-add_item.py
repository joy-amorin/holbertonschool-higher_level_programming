#!/usr/bin/python3
"""Load, add, save."""

import json
from os import path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    my_list = load_from_json_file('add_item.json')
else:
    my_list = []

for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json_file(my_list, 'add_item.json')
