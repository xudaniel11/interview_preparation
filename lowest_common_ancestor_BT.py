"""
Design an algorithm and write code to find the lowest common ancestor (meaning low in the tree)
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE:
This is not necessarily a binary search tree.
"""
import unittest


def lowest_common_ancestor(root, p, q):
    if not found(root, p) or not found(root, q):
        return None
    else:
        return find_lowest_common_ancestor(root, p, q)


def find_lowest_common_ancestor(root, p, q):
    if root == p and root == q:
        return root
    left_found_p = found(root.left, p)
    left_found_q = found(root.left, q)

    if left_found_p != left_found_q:
        return root

    child_side = root.left if left_found_q else root.right
    return find_lowest_common_ancestor(child_side, p, q)


def found(root, node):
    if root == None:
        return False
    elif root == node:
        return True
    else:
        return found(root.left, node) or found(root.right, node)


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
        result = lowest_common_ancestor(
            root, root.left.left, root.right.right)
        expected = root
        self.assertEqual(result, expected)

    def test_2(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        result = lowest_common_ancestor(
            root, root.left.left, root.left.right)
        expected = root.left
        self.assertEqual(result, expected)

    def test_3(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        other_tree_root = BinaryTreeNode('other')
        result = lowest_common_ancestor(
            root, root.left.left, other_tree_root)
        expected = None
        self.assertEqual(result, expected)

    def test_3(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        other_tree_root = BinaryTreeNode('other')
        result = lowest_common_ancestor(
            root, root.left.left, other_tree_root)
        expected = None
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
