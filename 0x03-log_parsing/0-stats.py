#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys
total_size = 0
status_dict = {
                '200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0,
            }
i = 0
for line in sys.stdin:
    line_array = line.split()
    i = i + 1
    total_size = int(line_array[-1]) + total_size
    status_dict[line_array[-2]] = int(status_dict[line_array[-2]]) + 1

    if i % 10 == 0:
        print("File size: {}".format(total_size))
        print('200: {}'.format(status_dict['200']))
        print('301: {}'.format(status_dict['301']))
        print('400: {}'.format(status_dict['400']))
        print('403: {}'.format(status_dict['403']))
        print('404: {}'.format(status_dict['404']))
        print('405: {}'.format(status_dict['405']))
        print('500: {}'.format(status_dict['500']))
