"""
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element
and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater
than sub-array B if sum(A) > sum(B).
"""
import unittest


def max_nonnegative_subarray(arr):
    N = len(arr)
    curr_sum = 0
    max_sum = 0
    start, end = 0, 0
    start_max, end_max = -1, -1
    possibilities = []

    while end < N:
        if arr[end] >= 0:
            curr_sum += arr[end]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start_max = start
                end_max = end + 1
            elif curr_sum == max_sum:
                if end + 1 - start > end_max - start_max:
                    start_max = start
                    end_max = end + 1
        else:
            start = end + 1
            curr_sum = 0
        end += 1

    if start_max == -1 or end_max == -1:
        return []
    else:
        return arr[start_max:end_max]


class TestMaxNonNegSubarray(unittest.TestCase):

    def test_case_1(self):
        A = [1, 2, 5, -7, 2, 3]
        result = max_nonnegative_subarray(A)
        answer = [1, 2, 5]
        self.assertEqual(result, answer)

    def test_case_2(self):
        A = [-1, -1, -1, -1, -1]
        result = max_nonnegative_subarray(A)
        answer = []
        self.assertEqual(result, answer)

    def test_case_3(self):
        A = [-3, 0, 1]
        result = max_nonnegative_subarray(A)
        answer = [0, 1]
        self.assertEqual(result, answer)

if __name__ == "__main__":
    unittest.main()
