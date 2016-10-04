"""
Get the diagonals of any N X M matrix.
"""

# starts top left and ends botton right


def matrix_antidiagonals(mat):
    n, m = len(mat[0]), len(mat)
    columns = zip(*mat)
    start_nums = mat[0][:-1]
    start_nums.extend(columns[-1])

    start_indices = [[0, x] for x in xrange(n)]
    start_indices.extend([[x, n - 1] for x in xrange(1, m)])

    result = []
    for index, tupl in enumerate(start_indices):
        i, j = tupl
        diagonal = [start_nums[index]]
        while i + 1 < m and j - 1 >= 0:
            diagonal.append(mat[i + 1][j - 1])
            i += 1
            j -= 1
        result.append(diagonal)
    return result


# starts top right and ends bottom left
def matrix_diagonals(mat):
    n, m = len(mat[0]), len(mat)
    columns = zip(*mat)
    start_nums = mat[0][1:]
    start_nums.reverse()
    start_nums.extend(columns[0])

    start_indices = [[0, x] for x in reversed(xrange(n))]
    start_indices.extend([[x, 0] for x in xrange(1, m)])

    result = []
    for index, tupl in enumerate(start_indices):
        i, j = tupl
        diagonal = [start_nums[index]]
        while i + 1 < m and j + 1 < n:
            diagonal.append(mat[i + 1][j + 1])
            i += 1
            j += 1
        result.append(diagonal)
    return result


import unittest


class TestMatrixDiagonals(unittest.TestCase):

    def test_antidiagonals(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        result = matrix_antidiagonals(mat)
        expected = [[1], [2, 4], [3, 5, 7], [6, 8, 10], [9, 11], [12]]
        self.assertEqual(result, expected)

    def test_diagonals(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        result = matrix_diagonals(mat)
        expected = [[3], [2, 6], [1, 5, 9], [4, 8, 12], [7, 11], [10]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
