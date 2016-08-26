"""
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1
On returning, the array A should be :

0 0 0
1 0 1
1 0 1

Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.
"""
import unittest
import copy
import numpy as np


def set_matrix_zeros_naive(mat):
    num_rows = len(mat)
    num_cols = len(mat[0])

    # gather location of all the zeros
    location_zeros = []
    for i in range(num_rows):
        for j in range(num_cols):
            if mat[i][j] == 0:
                location_zeros.append([i, j])

    # set rows and cols
    for num_row, num_col in location_zeros:
        mat[num_row] = [0] * num_cols
        for i in range(num_rows):
            mat[i][num_col] = 0

    return mat

"""
Better solution: iterate through each row and if there's a zero in it, set entire row to 0.
Then, iterate through col and if there's a zero in it, sett entire column to 0.
Time is O(M+N). Space is O(M*N) because I copied the matrix so that I could refer to it as the 'original'. 

A O(M*N) time and O(M+N) space solution would be to keep row_num and col_num arrays representing whether
there's a 0 in the ith row/jth col. Then, do a nested for loop iterating through the matrix and 
if row_num[i] or col_num[j], then set a 0 in matrix[i][j] 
"""


def set_matrix_zeros(mat):
    num_rows, num_cols = mat.shape
    reference_mat = copy.copy(mat)

    for num_row, row in enumerate(reference_mat):
        if 0 in row:
            mat[num_row] = [0] * num_cols

    for num_col, col in enumerate(reference_mat.T):
        if 0 in col:
            mat[:, num_col] = 0
    return mat


class TestSetMatrix(unittest.TestCase):

    def test_1(self):
        a = np.matrix([[1, 0, 1], [1, 1, 1], [1, 1, 1]])
        expected = np.matrix([[0, 0, 0], [1, 0, 1], [1, 0, 1]])
        result = set_matrix_zeros(a)
        np.testing.assert_array_equal(result, expected)

    def test_2(self):
        a = np.matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1]])
        expected = np.matrix(
            [[1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 0, 0]])
        result = set_matrix_zeros(a)
        np.testing.assert_array_equal(result, expected)

if __name__ == "__main__":
    unittest.main()
