"""
Find the inorder successor of a node in a binary search tree.

"""
import unittest


class BinarySearchTreeNode():

    def __init__(self, data):
        self.parent = None
        self.right = None
        self.left = None
        self.value = data


def inorder_sucessor(root, target_data):
    curr = find_node(root, target_data)
    if not curr:
        return None
    if curr.right:
        return find_in_right_subtree(curr.right)
    else:
        return find_deepest_ancestor(root, curr)


def find_node(root, target_data):
    if root == None:
        return None

    curr = root
    while curr:
        if curr.value == target_data:
            return curr
        elif curr.value > target_data:
            curr = curr.left
        elif curr.value < target_data:
            curr = curr.right
    return None


def find_in_right_subtree(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr


def find_deepest_ancestor(root, curr):
    parent = curr.parent
    ancestor = curr
    while parent:
        if parent.right == ancestor:
            ancestor = parent
            parent = parent.parent
        elif parent.left == ancestor:
            return parent
    return ancestor


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
        b.parent = a
        c.parent = a
        b.left = d
        b.right = e
        d.parent = b
        e.parent = b
        d.left = f
        e.left = g
        f.parent = d
        g.parent = e

        self.assertEqual(inorder_sucessor(a, 6), d)
        self.assertEqual(inorder_sucessor(a, 10), g)
        self.assertEqual(inorder_sucessor(a, 12), a)

    def test_2(self):
        a = BinarySearchTreeNode(6)
        b = BinarySearchTreeNode(3)
        c = BinarySearchTreeNode(10)
        d = BinarySearchTreeNode(4)
        e = BinarySearchTreeNode(5)
        f = BinarySearchTreeNode(3.5)
        g = BinarySearchTreeNode(4.5)

        a.left = b
        a.right = c
        b.parent = a
        c.parent = a
        b.right = d
        d.parent = b
        d.left = f
        d.right = e
        e.parent = d
        f.parent = d
        e.left = g
        g.parent = e

        self.assertEqual(inorder_sucessor(a, 6), c)
        self.assertEqual(inorder_sucessor(a, 5), a)

if __name__ == "__main__":
    unittest.main()
