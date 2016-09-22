"""
You have two very large binary trees: Tl, with millions of nodes, and T2, with
hundreds of nodes. Create an algorithm to decide ifT2 is a subtree of Tl.

A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of
n is identical to T2. That is, if you cut off the tree at node n, the two trees would
be identical.

Run time is O(N) to find where the starting matching root is. Then add on a 
O(km) where k is the number of times T2's root appears in T1. M is the number of nodes
in T2, N is the number of nodes in T1. So, run time is O(N+ km).

Soulution takes O(log(n) + log(m)) space??
"""
import unittest


def subtree_in_tree(root, subroot):
    if subroot == None:
        return True  # bc the empty subtree is always in a tree
    else:
        return find_match_start(root, subroot)


def find_match_start(root, subroot):
    if root == None:
        return False

    if root.val == subroot.val:
        return match_trees(root, subroot)
    else:
        return find_match_start(root.left, subroot) or find_match_start(root.right, subroot)


def match_trees(root, subroot):
    if root == None and subroot == None:
        return True
    if root == None or subroot == None:
        return False

    if root.val != subroot.val:
        return False
    else:
        return match_trees(root.left, subroot.left) and match_trees(root.right, subroot.right)


class BinaryTreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TestTreeInSubtree(unittest.TestCase):

    def test_1(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        root.left.left.left = BinaryTreeNode('H')
        root.left.left.right = BinaryTreeNode('I')
        root.left.right.left = BinaryTreeNode('J')
        root.left.right.right = BinaryTreeNode('K')
        root.right.left.left = BinaryTreeNode('L')
        root.right.left.right = BinaryTreeNode('M')
        root.right.right.left = BinaryTreeNode('N')
        root.right.right.right = BinaryTreeNode('O')

        subroot = BinaryTreeNode('C')
        subroot.left = BinaryTreeNode('F')
        subroot.left.left = BinaryTreeNode('L')
        subroot.left.right = BinaryTreeNode('M')

        result = subtree_in_tree(
            root, subroot)
        expected = False
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
