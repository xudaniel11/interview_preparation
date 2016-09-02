"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.

Example :

Input : [2, 3, -2, 4]
Return : 6

Possible with [2, 3]
"""
from operator import mul
import unittest


def max_product_subarray_WRONG(arr):
    # incorrect solution doesn't handle negative values (and how there can
    # be many of them in a resulting array) correctly
    result_indices = 0, 0
    maxsofar = -999999
    start, end = 0, 0
    while end < len(arr):
        print start, end, arr, maxsofar
        product = reduce(mul, arr[start:end + 1])
        if product >= maxsofar:
            maxsofar = product
            end += 1
            result_indices = start, end
        elif product < maxsofar:
            start += 1
            end = start
    return maxsofar

# following solution taken from interviewbit.com


def max_product_subarray(arr):
    max_ending_here = 1
    min_ending_here = 1
    max_so_far = 1
    n = len(arr)
    if n == 0:
        return 0
    for i in range(n):
        if arr[i] > 0:
            max_ending_here = max_ending_here * arr[i]
            min_ending_here = min(min_ending_here * arr[i], 1)
        elif arr[i] == 0:
            # reset bc multiplying by 0 won't give us the max product
            max_ending_here = 1
            min_ending_here = 1
        elif arr[i] < 0:
                #
            temp = max_ending_here
            max_ending_here = max(min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    if max_so_far == 1:
        if 1 in arr:
            # either 1 is literally the biggest product
            return 1
        else:
            # or all the arr values are <= 0
            return 0
    # or the traditional case, when result > 0
    return max_so_far


class TestMaxProduct(unittest.TestCase):

    def test_1(self):
        a = [0, 0, 0]
        result = max_product_subarray(a)
        expected = 0
        self.assertEqual(result, expected)

    def test_2(self):
        a = [1, 0, 0, 0, 0, 0, -2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, -1, -2, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, -2, 3, 0, 0, 0, 0, 0, 0, -2, -3, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, -2, 0, 0, 0, 2, -3, 0, 0, 0, 0]
        result = max_product_subarray(a)
        expected = 9
        self.assertEqual(result, expected)

    def test_3(self):
        a = [1, -2, -3, 0, 7, -8, -2]
        result = max_product_subarray(a)
        expected = 112
        self.assertEqual(result, expected)

    def test_4(self):
        a = [-4, 0, -5, 0]
        result = max_product_subarray(a)
        expected = 0
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
