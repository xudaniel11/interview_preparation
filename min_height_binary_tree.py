"""
Given a sorted (increasing order) array, write an algorithm to create a binary 
tree with minimal height.

CTCI pg 54
"""
import unittest 

def create_tree(arr, start, end):
	if end < start:
		return None 
	mid = (start+end)//2
	new_node = BST_Node(arr[mid])
	new_node.left = create_tree(arr, start, mid-1)
	new_node.right = create_tree(arr, mid+1, end)
	return new_node

def create_minimal_BST(arr):
	return create_tree(arr, 0, len(arr)-1)

class BST_Node():
	def __init__(self, val):
		self.val = val
		self.left = None 
		self.right = None

	def print_tree(self):
		q = [self]
		while len(q) > 0:
			curr = q.pop(0)
			print curr.val,
			if curr.left:
				q.append(curr.left)
			if curr.right:
				q.append(curr.right)

class Test_Min_BST(unittest.TestCase):
	def test_case_1(self):
		ex1 = [1,2,3,4,5,6,7]
		root = create_minimal_BST(ex1)
		root.print_tree() #level order print should be 4,2,6,1,3,5,7
		print "\n"
		self.assertEqual(root.val, 4) 

	def test_case_2(self):
		ex2 = [1,1,1]
		root = create_minimal_BST(ex2)
		root.print_tree()  #level order print should be 1,1,1
		print "\n"
		self.assertEqual(root.val, 1)


	def test_case_3(self):
		ex3 = [1,1,2,2]
		root = create_minimal_BST(ex3)
		root.print_tree() #level order print should be 1 1 2 2
		print "\n"
		self.assertEqual(root.val, 1)

if __name__ == "__main__":
	unittest.main()

