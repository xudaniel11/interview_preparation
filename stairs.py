"""
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1, 2, or 3 stairs at a time. Count the number
of ways, the person can reach the top.

Base cases handle illegal cases.
"""


def stairs(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return stairs(n - 1) + stairs(n - 2) + stairs(n - 3)

print stairs(4)  # should be 7
print stairs(5)  # should be 13
