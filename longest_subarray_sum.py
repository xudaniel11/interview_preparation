"""
Find the longest contiguous subarray that sums up to k.

Current solution is the naive one: get all the different combinations of lists that sum up to k and then return the longest one.
O(N^2) 

Is there a faster solution?
"""
import unittest

def longest_subarray_sum_naive(arr, k):
	subarray_combinations = []
	for i in range(len(arr)):
		for j in range(len(arr)):
			subarray_combinations.append(arr[i:j+1])

	possible_arrays = []
	for subarray in subarray_combinations:
		if sum(subarray) == k:
			possible_arrays.append(subarray)

	return max(possible_arrays, key=len) if len(possible_arrays) > 0 else []

class TestLongestSubarraySum(unittest.TestCase):
	def test_naive0(self):
		ex0 = [3,2,-1,5,4,-4,0,7]
		result = longest_subarray_sum_naive(ex0, 4)
		self.assertEqual(result, [-1,5,4,-4,0])

	def test_naive1(self):
		ex1 = [3,2,-1,5,-1,5,7,1]
		result = longest_subarray_sum_naive(ex1, 4)
		self.assertEqual(result, [3,2,-1])

	def test_naive2(self):
		ex2 = [0,0,0,0,0,0,1]
		result = longest_subarray_sum_naive(ex2,1)
		self.assertEqual(result, ex2)

	def test_null_case(self):
		ex3 = [0]
		result = longest_subarray_sum_naive(ex3, 5)
		self.assertEqual(result, [])
if __name__ == '__main__':
	unittest.main()

