"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example :

Input : 
   1
  /  \
 2    3

Output : False


Input : 
  2
 / \
1   3

Output : True

"""
import unittest


def is_valid(node, min_val, max_val):
    if node == None:
        return True

    if node.val < min_val or node.val > max_val:
        return False

    return (is_valid(node.left, min_val, node.val - 1)) and is_valid(node.right, node.val + 1, max_val)


class BinarySearchTreeNode():

    def __init__(self, data):
        self.right = None
        self.left = None
        self.val = data


class TestInorderSuccessor(unittest.TestCase):

    def test_1(self):
        """
              15(a)
             /   \
            10(b) 20(c)
           /    \
         d(8)   12(e)
         /\    /
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

        self.assertEqual(is_valid(a, -999, 999), True)

    def test_2(self):
        """
              35(a)
             /   \
            10(b) 20(c)

        """
        a = BinarySearchTreeNode(35)
        b = BinarySearchTreeNode(10)
        c = BinarySearchTreeNode(20)

        a.left = b
        a.right = c

        self.assertEqual(is_valid(a, -999, 999), False)

if __name__ == "__main__":
    unittest.main()
