"""
Given an array of integers arr, write a function that returns another array at the same length where the value at each index i is the product of all array values except arr[i].

Solve without using division and analyze the runtime and space complexity

Example: given the array [2, 7, 3, 4]
your function would return: [84, 24, 56, 42] (by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3])

Algorithm should run in O(N) time.

Solution: create two arrays representing the direction we iterate in. Each element in each array represents 
the product so far from a particular direction up to that index.

"""


def get_array_of_array_products(arr):
    going_right = [1]
    for i in range(1, len(arr)):
        going_right.append(going_right[i - 1] * arr[i - 1])

    going_left = [1]
    for i in range(1, len(arr)):
        going_left.append(going_left[i - 1] * arr[len(arr) - i])
    going_left.reverse()

    return [x * y for x, y in zip(going_left, going_right)]

print get_array_of_array_products([2, 4, 6, 7])  # should be [168, 84, 56, 48]
