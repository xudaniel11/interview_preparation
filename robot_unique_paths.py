"""
A robot is located at the top-left corner of an M X N grid. The robot can only move either down or
right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

Input: M, N representing the number of rows and cols, respectively
Output: an integer

bottom-up DP solution from http://articles.leetcode.com/unique-paths/

tldr; the total unique paths at grid (i,j) is equal to the sum of total unique paths from grid to the right (i,j+1) and the grid below (i+1,j).

"""
import numpy as np
import unittest


def get_num_unique_paths(M, N):
    mat = np.zeros((M, N))
    mat[M - 1] = np.ones((1, N))
    mat[:, N - 1] = np.ones(M)

    for i in reversed(xrange(M - 1)):
        for j in reversed(xrange(N - 1)):
            right = mat[i, j + 1]
            down = mat[i + 1, j]
            mat[i, j] = right + down
    return int(mat[0, 0])


"""
Follow up: 
Imagine certain spots are "off limits," such that the robot cannot step
on them. Design an algorithm to find a path for the robot from the top
left to the bottom right.

Solution: make blocks 0.
"""


def robot(grid):
    m, n = grid.shape
    for i in reversed(range(m - 1)):
        for j in reversed(range(n - 1)):
            if grid[i, j] == 0:
                continue
            else:
                grid[i, j] = grid[i, j + 1] + grid[i + 1, j]
    return grid[0, 0]


class TestUniquePaths(unittest.TestCase):

    def test_1(self):
        result = get_num_unique_paths(3, 7)
        expected = 28
        self.assertEqual(result, expected)

    def test_blocks(self):
        mat = np.ones((3, 4))
        mat[1, 0] = 0
        result = robot(mat)
        expected = 6
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
