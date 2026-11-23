#!/usr/bin/python3
"""Module that calculates the fewest operations needed to get n 'H'."""


def minOperations(n):
    """Return the fewest number of operations to get exactly n 'H'.

    The only operations are Copy All and Paste. The answer is the sum of
    the prime factors of n. Return 0 if n is impossible to achieve.
    """
    if not isinstance(n, int) or n < 2:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
