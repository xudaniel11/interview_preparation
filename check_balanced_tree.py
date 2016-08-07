"""
Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
from the root by more than one.

Solution taken from CTCI: recursive algorithms calculate the maximum and minimum length
paths in the tree. Compare the two at the end.

"""
import unittest

def max_depth(node):
	if node == None:
		return 0
	else:
		return 1 + max(max_depth(node.left), max_depth(node.right))

def min_depth(node):
	if node == None:
		return 0
	else:
		return 1 + min(min_depth(node.left), min_depth(node.right))

def check_balanced_tree(node):
	return max_depth(node) - min_depth(node) <= 1

class BinaryTreeNode():
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None

class Test_Balanced_Tree(unittest.TestCase):
	def case_1(self):
		root = BinaryTreeNode('A')
		root.left = BinaryTreeNode('B')
		root.right = BinaryTreeNode('C')
		root.right.left = BinaryTreeNode('F')
		root.right.right = BinaryTreeNode('G')
		root.left.left = BinaryTreeNode('D')
		root.left.right = BinaryTreeNode('E')
		result = check_balanced_tree(root)
		self.assertEqual(result, True)

	def case_2(self):
		root = BinaryTreeNode('A')
		root.left = BinaryTreeNode('B')
		root.right = BinaryTreeNode('C')
		root.right.left = BinaryTreeNode('F')
		root.right.right = BinaryTreeNode('G')
		result = check_balanced_tree(root)
		self.assertEqual(result, False)

if __name__ == "__main__":
	unittest.main()