"""
Given a binary tree, invert the binary tree and return it.
Look at the example for more details.

Example :
Given binary tree

     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return

     1
   /   \
  3     2
 / \   / \
7   6 5   4

"""
import unittest


def invert_BST(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root


def print_bst(root):
    q = [root]
    while q:
        curr = q.pop(0)
        print curr.val,
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


class BinarySearchTreeNode():

    def __init__(self, data):
        self.right = None
        self.left = None
        self.val = data


class TestInvertBST(unittest.TestCase):

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

        result = invert_BST(a)
        print print_bst(result)  # should be 15, 20, 10, 12, 8, 11, 6


if __name__ == "__main__":
    unittest.main()
