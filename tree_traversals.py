import unittest


def level_order(node):  # root, children
    q = [node]
    while len(q) > 0:
        curr = q.pop(0)
        print curr.val,
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return node


def inorder(node):  # left, root, then right
    if node != None:
        if node.left:
            inorder(node.left)
        print node.val,
        if node.right:
            inorder(node.right)


def preorder(node):  # root, left, then right
    if node != None:
        print node.val,
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)


def postorder(node):  # left, right, then root
    if node != None:
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        print node.val,


def dfs_iterative(node):
    stack = [node]
    while stack:
        curr = stack.pop()
        print curr.val,
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


def bfs_iterative(node):
    q = [node]
    while q:
        curr = q.pop(0)
        print curr.val,
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


class BinaryTreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TestTreeTraversals(unittest.TestCase):

    def test_level_order(self):
        root = BinaryTreeNode(0)
        root.left = BinaryTreeNode(1)
        root.right = BinaryTreeNode(2)
        root.left.left = BinaryTreeNode(3)
        root.left.right = BinaryTreeNode(4)
        print "should be 0, 1, 2, 3, 4: "
        level_order(root)
        print "\n"

    def test_inorder(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        print "should be D,B,E,A,F,C,G: "
        inorder(root)
        print "\n"

    def test_preorder(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        print "should be A,B,D,E,C,F,G: "
        preorder(root)
        print "\n"

    def test_postorder(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        print "should be D,E,B,F,G,C,A: "
        postorder(root)
        print "\n"

    def test_DFS_iterative(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        print "should be A,B,D,E,C,F,G"
        dfs_iterative(root)
        print "\n"

    def test_BFS_iterative(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        print "should be A,B,C,D,E,F,G"
        bfs_iterative(root)
        print "\n"

if __name__ == '__main__':
    unittest.main()
