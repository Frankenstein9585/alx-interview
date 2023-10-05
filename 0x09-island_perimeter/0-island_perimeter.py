#!/usr/bin/python3
"""Solves the Island Perimeter interview question"""


def island_perimeter(grid):
    """Solves the Island Perimeter problem"""
    visit = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1


print(island_perimeter([[0, 1, 0, 0],
                        [1, 1, 1, 0],
                        [0, 1, 0, 0],
                        [1, 1, 0, 0]]))
