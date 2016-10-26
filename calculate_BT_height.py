"""
Calculate height of a binary tree.
"""
import unittest


def calculate_height(node):
    if node == None:
        return 0

    left, right = 1, 1
    if node.left:
        left = 1 + calculate_height(node.left)
    if node.right:
        right = 1 + calculate_height(node.right)

    return max(left, right)


class BinaryTreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TestFirstCommonAncestor(unittest.TestCase):

    def test_1(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        result = calculate_height(root)
        expected = 3
        self.assertEqual(result, expected)

    def test_2(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        root.left.left.left = BinaryTreeNode('F')
        root.left.left.right = BinaryTreeNode('G')
        root.left.left.left.left = BinaryTreeNode('H')
        result = calculate_height(root)
        expected = 5
        self.assertEqual(result, expected)

    def test_3(self):
        root = BinaryTreeNode('A')
        result = calculate_height(root)
        expected = 1
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()
