"""
You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.

Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).

Example :

Input : 
	S = [1, 2, 3] 
	N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}	
Note that the answer can overflow. So, give us the answer % 1000007
"""
import numpy as np
import unittest


def count_change(denominations, target):
    # We need m+1 cols bc the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    n, m = len(denominations), target + 1
    mat = np.zeros((n, m))

    # 0th col initialized to 1 bc there's only 1 way of making change for $0
    mat[:, 0] = 1
    for i in range(n):
        coin = denominations[i]
        for j in range(1, m):
            # Number of solutions including the current coin
            left = mat[i, j - coin] if j - coin >= 0 else 0
            # Number of solutions excluding the current coin
            top = mat[i - 1, j] if j >= 1 else 0
            mat[i, j] = left + top

    return int(mat[-1, -1]) % 1000007


class TestCountChange(unittest.TestCase):

    def test_1(self):
        a = [18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8]
        b = 458
        result = count_change(a, b)
        expected = 867621
        self.assertEqual(result, expected)

    def test_2(self):
        a = [2, 3]
        b = 5
        result = count_change(a, b)
        expected = 1
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
