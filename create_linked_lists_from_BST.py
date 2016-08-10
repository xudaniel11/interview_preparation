"""
Given a binary search tree, design an algorithm which creates a linked list of
all the nodes at each depth (eg, if you have a tree with depth D, you'll have D linked lists)

CTCI pg 54

lots of leaky abstractions in this code :(
"""
import unittest 

def create_linked_lists_from_BST(root):
	level = 0
	result = []
	lst = LinkedList()
	lst.add(root)
	result.append((level, lst)) # a list of tuples where 0th element is the level and 1st is a LinkedList of BinaryTreeNodes
	while True:
		lst = LinkedList()
		nodes_on_same_level = result[level][1]
		for node in nodes_on_same_level.list():
			if node != None:
				if node.left != None:
					lst.add(node.left)
				if node.right != None:
					lst.add(node.right)
		if lst.size > 0:
			result.append((level+1, lst))
		else:
			break
		level+=1
	return result

class LinkedList():
	def __init__(self):
		self.lst = []
		self.size = 0

	def add(self, node):
		self.lst.append(node)
		self.size += 1

	def list(self):
		return self.lst

class BinaryTreeNode():
	def __init__(self, val):
		self.val = val
		self.left = None 
		self.right = None

class Test_Create_LL_from_BST(unittest.TestCase):
	def test_case_1(self):
		root = BinaryTreeNode('A')
		root.left = BinaryTreeNode('B')
		root.right = BinaryTreeNode('C')
		root.right.left = BinaryTreeNode('F')
		root.right.right = BinaryTreeNode('G')
		root.left.left = BinaryTreeNode('D')
		root.left.right = BinaryTreeNode('E')
		result = create_linked_lists_from_BST(root)
		for result in result:
			ll = result[1]
			print list(map(lambda x: x.val, ll.list()))

if __name__ == "__main__":
	unittest.main()

