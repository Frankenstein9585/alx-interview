#!/usr/bin/python3
"""Implementation of N-Queens Problem"""
import sys


def solve_n_queens(n: int) -> list[list[int]]:
    """Function to solve N-Queens Problem"""
    col = set()
    pos_diag = set()  # positive diagonal (row + column)
    neg_diag = set()  # negative diagonal (row - column)

    result = []
    board = [['.'] * n for _ in range(n)]

    def backtrack(r):
        """Recursive function that handles row checking"""
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 'Q'

            backtrack(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = '.'

    backtrack(0)
    return result


try:
    args = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

elif args < 4:
    print("N must be at least 4")
    sys.exit(1)

boards = solve_n_queens(args)
index_result = [[] for _ in range(len(boards))]
for i in range(len(index_result)):
    for row in boards[i]:
        index_result[i].append([boards[i].index(row), row.index('Q')])

for solution in index_result:
    print(solution)
