#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D Matrix in place"""
    copy = [row[:] for row in matrix]
    size = len(matrix)
    j = -1
    for row in copy:
        for i in range(size):
            matrix[i][j] = row[i]
        j -= 1
