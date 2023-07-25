#!/usr/bin/python3
"""
Funtion to demonstrate pascal's triangle
"""
def pascal_triangle(n):
    """This function returns Pascal's triangle"""
    if n <= 0:
        return []
    pascal_list = [[1]]
    while len(pascal_list) < n:
        last_row = pascal_list[-1]
        new_row = [1]
        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])
        new_row.append(1)
        pascal_list.append(new_row)
    return pascal_list
