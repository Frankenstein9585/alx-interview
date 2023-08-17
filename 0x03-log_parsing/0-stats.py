#!/usr/bin/python3
"""This script reads stdin line by line and computes some metrics"""
import sys

status_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

file_size = 0


def print_metrics():
    """prints of the logs"""
    print("File size: {}".format(file_size))
    for status in sorted(status_dict.keys()):
        if status_dict[status]:
            print("{}: {}".format(status, status_dict[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in sys.stdin:
            try:
                elems = line.split()
                file_size += int(elems[-1])
                if elems[-2] in status_dict:
                    status_dict[elems[-2]] += 1
            except Exception:
                pass
            if count == 9:
                print_metrics()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_metrics()
        raise
    print_metrics()
