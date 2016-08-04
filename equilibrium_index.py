"""
Watson gives Sherlock an array  of length. Then he asks him to determine if there 
exists an element in the array such that the sum of the elements on its left is 
equal to the sum of the elements on its right. If there are no elements to the 
left/right, then the sum is considered to be zero. 
"""

import unittest

def equilibrium_index(arr):
	going_right = [arr[0]]
	going_left = [arr[-1]]
	for i, num in enumerate(arr):
		if i == 0:
			continue
		else:
			going_right.append(going_right[i-1]+arr[i])
			going_left.append(arr[len(arr)-1-i] + going_left[i-1])
	going_left.reverse()

	for i, num in enumerate(arr):
		if going_right[i] == going_left[i]:
			return i


class TestEquilibriumIndex(unittest.TestCase):
	def test_usual_case(self):
		a = [1,4,3,7,6,2]
		self.assertEqual(equilibrium_index(a), 3)

if __name__ == '__main__':
	unittest.main()