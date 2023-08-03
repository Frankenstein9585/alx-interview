#!/usr/bin/python3
"""This file contains a method that solves the lockboxes problem"""


def canUnlockAll(boxes):
    """This function solves the lockboxes problem"""
    n = len(boxes)
    boxes_unlocked = set()
    stack = [0]  # Start with box 0

    while stack:
        box = stack.pop()
        boxes_unlocked.add(box)

        for key in boxes[box]:
            if key not in boxes_unlocked and key < n:
                stack.append(key)

    return len(boxes_unlocked) == n
