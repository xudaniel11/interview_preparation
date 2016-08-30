"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem

Algorithm does binary search until it finds the right row, then binary search again to find 
value in the row. Time: O(log M + log N), Space: O(N)
"""
import numpy as np


def matrix_search(mat, target):
    N, M = mat.shape
    start_row = 0
    end_row = N - 1
    while start_row <= end_row:
        mid = (start_row + end_row) / 2
        mid_row = np.array(mat[mid])[0].tolist()
        if mid_row[0] <= target <= mid_row[-1]:
            return binary_search(mid_row, target)
        elif target > mid_row[-1]:
            start_row = mid + 1
        elif target < mid_row[0]:
            end_row = mid - 1
    return 0


def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == target:
            return 1
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
    return 0

a = np.matrix([
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
])
print matrix_search(a, 11)
