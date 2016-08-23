"""
Given a 2-dimensional array of positive and negative integers, find the sub-rectangle with the largest sum.
The sum of a rectangle is the sum of all the elements in that rectangle. In this problem the sub-rectangle
with the largest sum is referred to as the maximal sub-rectangle. A sub-rectangle is any contiguous sub-array
of size 1*1 or greater located within the whole array. As an example, the maximal sub-rectangle of the array:

 0 -2 -7  0
 9  2 -6  2
-4  1 -4  1
-1  8  0 -2

is in the lower left hand corner:

9  2
-4  1
-1  8

and has a sum of 15.

Find the sum of the maximum subrectangle.

Runtime: O(col^2 * row)
Space: O(row)
"""
import numpy as np
import unittest


def find_max_sum_submatrix(mat):
    n, m = mat.shape
    maxLeft, maxRight, maxUp, maxDown, maxSum = 0, 0, 0, 0, 0
    for i, left_col in enumerate(mat.T):
        tmp_col = left_col.copy()
        for j in range(i, m):
            right_col = mat[:, j].transpose()
            if not np.array_equal(left_col, right_col):
                tmp_col += right_col
            up, down, col_max = max_sum_subarray(tmp_col)
            if col_max > maxSum:
                maxLeft = i
                maxRight = j
                maxUp = up
                maxDown = down
                maxSum = col_max
    # print maxUp, maxDown, maxLeft, maxRight
    result_mat = mat[maxUp:maxDown + 1, maxLeft:maxRight + 1]
    # print result_mat
    return np.sum(result_mat)


def max_sum_subarray(col):
    max_here = col[0, 0]
    max_so_far = col[0, 0]
    start, end = 0, 0
    for index, num in np.ndenumerate(col):
        i = index[1]
        if i == 0:
            continue
        if max_so_far < num and num >= max_so_far + num:
            max_here = num
            start = i
            end = i
        else:
            max_here += num
        if max_here > max_so_far:
            max_so_far = max_here
            end = i
    return start, end, max_so_far


class TestMaxSumSubrectangle(unittest.TestCase):

    def test_case_helper(self):
        a = np.matrix([[-3, -1, 2, 7, 5]])
        result = max_sum_subarray(a)
        expected = (2, 4, 14)
        self.assertEqual(result, expected)

    def test_case_1(self):
        a = np.matrix([[0, -2, -7, 0], [9, 2, -6, 2],
                       [-4, 1, -4, 1], [-1, 8, 0, -2]])
        result = find_max_sum_submatrix(a)
        expected = 15
        self.assertEqual(result, expected)

    def test_case_2(self):
        a = np.matrix([[1, 2, -1, -4, -20],
                       [-8, -3, 4, 2, 1],
                       [3, 8, 10, 1, 3],
                       [-4, -1, 1, 7, -6]])
        result = find_max_sum_submatrix(a)
        expected = 29
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
