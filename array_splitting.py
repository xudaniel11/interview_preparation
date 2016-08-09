"""
Nikita just came up with a new array game. The rules are as follows:

Initially, there is an array, , containing  integers.

In each move, Nikita must partition the array into  non-empty parts such that the sum of the elements in the left partition is equal to the sum of the elements in the right partition. If Nikita can make such a move, she gets  point; otherwise, the game ends.

After each successful move, Nikita discards either the left partition or the right partition and continues playing by using the remaining partition as array .

Nikita loves this game and wants your help getting the best score possible. Given , can you find and print the maximum number of points she can score?
"""
import unittest

def array_splitting(arr):
	if len(arr) == 1:
		return 0

	going_left = [arr[0]]
	going_right = [arr[-1]]

	for i in range(1,len(arr)):
		going_left.append(going_left[i-1]+arr[i])
 	for i in range(1, len(arr)):
 		going_right.append(going_right[i-1]+arr[len(arr)-i-1])
 	going_right.reverse()

 	for i in range(len(arr)-1):
	 	if going_left[i] == going_right[i+1]:
	 		split_index = i
	 		return 1 + max(array_splitting(arr[:split_index+1]), array_splitting(arr[split_index+1:]))
	return 0

class TestArraySplitting(unittest.TestCase):
	def test_case_1(self):
		ex1 = [6,3,2,1,5,5,2]
		result = array_splitting(ex1)
		self.assertEqual(result, 3)

	def test_case_2(self):
		ex2 = [1,1,2,4,8,16]
		result = array_splitting(ex2)
		self.assertEqual(result, 5)

	def test_case_3(self):
		ex3=[1,1,1,1,1,1,1,1]
		result = array_splitting(ex3)
		self.assertEqual(result, 3)

if __name__ == "__main__":
	unittest.main()
