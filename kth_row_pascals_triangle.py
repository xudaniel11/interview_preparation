"""
Given an index k, return the kth row of the Pascal's triangle.

Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A['C-1] from previous row R - 1.

Time: O(K^2)?
Space: O(K^2)?
"""
import unittest


def get_kth_row_pascals(k):
    triangle_rows = [[1], [1, 1]]
    for i in xrange(2, k + 1):
        ith_row = [1]
        for j, num in enumerate(xrange(i - 1)):
            prev_row = triangle_rows[i - 1]
            ith_row.append(prev_row[j] + prev_row[j + 1])
        ith_row.append(1)
        triangle_rows.append(ith_row)
    return triangle_rows[k]


class TestPascals(unittest.TestCase):

    def test_case_1(self):
        expected_answer = [1, 3, 3, 1]
        result = get_kth_row_pascals(3)
        self.assertEqual(expected_answer, result)

    def test_case_2(self):
        expected_answer = [1, 5, 10, 10, 5, 1]
        result = get_kth_row_pascals(5)
        self.assertEqual(expected_answer, result)
if __name__ == "__main__":
    unittest.main()
