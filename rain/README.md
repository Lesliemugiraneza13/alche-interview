# Rain

`0-rain.py` defines `rain(walls)`, which takes a list of non-negative
integers (the heights of walls of width 1) and returns how many square units
of water are retained after it rains. The ends of the list are not walls and
retain no water. An empty list returns `0`.

The function uses two pointers that move inward from both ends. The water
above a wall is limited by the shorter of the tallest walls on its left and
on its right, so the pointer on the shorter side is always the one that moves.
It runs in O(n) time and uses no imported module.

Example:

```
rain([0, 1, 0, 2, 0, 3, 0, 4])  # 6
rain([2, 0, 0, 4, 0, 0, 1, 0])  # 6
```
