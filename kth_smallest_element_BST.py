"""
Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST 
"""
import unittest
from more_itertools import unique_everseen


class BinarySearchTreeNode():

    def __init__(self, data):
        self.right = None
        self.left = None
        self.val = data


def kth_smallest_elem(node, k):
    ls = inorder_traversal(node)
    # unique_everseen removes duplicates from a list in O(N) time accorinding
    # to
    # http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
    result = list(unique_everseen(ls))
    return result[k - 1]


def inorder_traversal(node, result=[]):
    if node == None:
        return

    if node.left:
        inorder_traversal(node.left, result)
    result.append(node.val)
    if node.right:
        inorder_traversal(node.right, result)
    return result


class TestKthSmallest(unittest.TestCase):

    def test_1(self):
        """
              15(a)
             /   \
            10(b) 20(c)
           /    \
         d(8)   12(e)
          \    /
         f(6) 11(g)

        """
        a = BinarySearchTreeNode(15)
        b = BinarySearchTreeNode(10)
        c = BinarySearchTreeNode(20)
        d = BinarySearchTreeNode(8)
        e = BinarySearchTreeNode(12)
        f = BinarySearchTreeNode(6)
        g = BinarySearchTreeNode(11)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        d.left = f
        e.left = g

        result = kth_smallest_elem(a, 2)
        self.assertEqual(result, d.val)

    def test_2(self):
        a = BinarySearchTreeNode(-1)
        b = BinarySearchTreeNode(-1)
        c = BinarySearchTreeNode(3)
        d = BinarySearchTreeNode(-1)
        e = BinarySearchTreeNode(4)
        f = BinarySearchTreeNode(5)

        a.left = b
        a.right = c
        b.left = d
        c.left = e
        c.right = f

        result = kth_smallest_elem(a, 1)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()
