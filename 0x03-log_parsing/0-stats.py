#!/usr/bin/python3
"""This script reads stdin line by line and computes some metrics"""
import re
import sys

number_of_lines = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
total_file_size = 0
status_dict = {}
for code in status_codes:
    status_dict[code] = 0
format_pattern = (r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
                  r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET '
                  r'/projects/260 HTTP/1\.1" \d{3} \d+')

try:
    for line in sys.stdin:
        if not re.match(format_pattern, line):
            pass
        # increase number of lines
        number_of_lines += 1
        # increase total file size
        file_size = line.split()[-1]
        total_file_size += int(file_size)
        status_code = int(line.split()[-2])
        status_dict[status_code] += 1
        if number_of_lines % 10 == 0:
            print('File size:', total_file_size)
            for k, v in status_dict.items():
                if v != 0:
                    print('{}: {}'.format(k, v))

except KeyboardInterrupt:
    print('File size:', total_file_size)
    for k, v in status_dict.items():
        if v != 0:
            print('{}: {}'.format(k, v))
