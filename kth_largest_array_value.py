"""
Select Kth largest value in the array. Given an unsorted array of size n, and a value k. Select the kth largest value from the array. 

For example: 

Array is [5, 3, 9, 1], n is 4 
k = 0 => 9 
k = 1 => 5 
k = 3 => 1

Algorithm: initialize a MinHeap of size k. Then iterate over the rest of the arr: if arr[i] > MinHeap root (the smallest element), pop that root and 
add arr[i]. Bubble arr[i] to its correct position in the heap. At the end, return the item at the MinHeap root. This works because by using a MinHeap
and updating it with larger values, we will always have the kth largest elements in the MinHeap.

Time: (O(klogk) to build heap + O(logk) for removals + O(logk) for insertions) * N for each element in the array = O(N*logk).
Space: O(k)

Apparently this can be done in O(N) time?
"""
import Heap 
import unittest

def kth_largest_array_value(arr, k):
	n = len(arr)
	if k > n:
		return None

	heap = Heap.Heap()
	heap.buildHeap(arr[:k])
	for i in range(k, n-k):
		heap.insert(arr[i + k])
		if arr[i] > heap.peek_root():
			heap.extractMin()
			heap.insert(arr[i])
	return heap.peek_root()

class TestTreeTraversals(unittest.TestCase):
	def case_1(self):
		arr = [3,4,1,2,6]
		result = kth_largest_array_value(arr, k)
		assertEqual(result, 3)

	def case_2(self):
		arr = [5,3,9,1]
		result = kth_largest_array_value(arr, 2)
		assertEqual(result, 2)

	def null_case1(self):
		arr = []
		result = kth_largest_array_value(arr, 1)
		assertEqual(result, None)

	def case_3(self):
		arr = [1,1,1,1,1]
		result = kth_largest_array_value(arr, 2)
		assertEqual(result, 1)

if __name__ == '__main__':
	unittest.main()