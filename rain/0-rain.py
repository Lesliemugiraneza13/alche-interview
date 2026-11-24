#!/usr/bin/python3
"""Module that calculates how much rainwater is retained between walls."""


def rain(walls):
    """Return the total units of water retained by a list of wall heights.

    Two pointers move inward from both ends. The water above a wall is
    limited by the lower of the tallest walls to its left and to its right.
    The ends of the list are not walls, so they retain no water.
    """
    if not walls:
        return 0
    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    total = 0
    while left < right:
        if walls[left] < walls[right]:
            left += 1
            left_max = max(left_max, walls[left])
            total += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            total += right_max - walls[right]
    return total
