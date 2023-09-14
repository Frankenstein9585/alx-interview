#!/usr/bin/python3
"""Rotate 2D Matrix"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """Rotates a 2D Matrix in place"""
    copy = [row[:] for row in matrix]
    size = len(matrix)
    j = -1
    for row in copy:
        for i in range(size):
            matrix[i][j] = row[i]
        j -= 1


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


rotate_2d_matrix(matrix)

print(matrix)
