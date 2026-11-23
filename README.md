# Minimum Operations

`0-minoperations.py` defines `minOperations(n)`, which returns the fewest
number of `Copy All` and `Paste` operations needed to go from a single `H`
to exactly `n` `H` characters. It returns `0` if `n` is impossible (`n < 2`).

The result is the sum of the prime factors of `n`: each prime factor `p`
costs one `Copy All` plus `p - 1` `Paste` operations, i.e. `p` operations.

Example: `9 = 3 x 3`, so `3 + 3 = 6` operations.
