#!/usr/bin/python3
"""Solves the Island Perimeter interview question"""


def island_perimeter(grid: list[list[int]]) -> int:
    """Solves the Island Perimeter problem"""
    perimeter = 0
    for i in range(len(grid)):
        if i == 0 or i == len(grid) - 1:
            continue
        for j in range(len(grid[i])):
            if j == 0 or j == len(grid[i]) - 1:
                continue
            if grid[i][j] == 0:
                continue
            if grid[i][j] == 1:
                # check all four surrounding elements
                if grid[i - 1][j] == 0:  # up
                    perimeter += 1
                if grid[i][j - 1] == 0:  # left
                    perimeter += 1
                if grid[i][j + 1] == 0:  # right
                    perimeter += 1
                if grid[i + 1][j] == 0:  # down
                    perimeter += 1
    return perimeter


