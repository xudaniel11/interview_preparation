"""
Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE:
This is not necessarily a binary search tree.
"""
import unittest


def first_common_ancestor(root, p, q):
    if not found(root, p) or not found(root, q):
        return None
    else:
        return find_first_common_ancestor(root, p, q)


def find_first_common_ancestor(root, p, q):
    if root == p and root == q:
        return root
    left_found_p = found(root.left, p)
    left_found_q = found(root.left, q)

    if left_found_p != left_found_q:
        return root

    child_side = left_found_q ? root.left else root.right
    return find_first_common_ancestor(child_side, p, q)


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
