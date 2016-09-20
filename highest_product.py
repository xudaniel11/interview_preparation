"""
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

Input:

array of integers e.g {1, 2, 3}
 NOTE: Solution will fit in a 32-bit signed integer
Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000
"""


def max_prod3(arr):
    arr.sort()
    if len(arr) < 3:
        return 0
    m1, m2, m3 = arr[-1], arr[-2], arr[-3]
    result = m1 * m2 * m3
    if arr[0] < 0 and arr[1] < 0:
        tmp = arr[0] * arr[1] * m1
        if tmp > result:
            result = tmp
    return result

print max_prod3([1, 3, 5, 2, 8, 0, -1, -3])
print max_prod3([-1, -2, -3, -4, -5])
