"""
Print the length of the longest consecutive path in an n-ary tree.
1 -> 2 -> 3 is consecutive.
1 -> 3 is not.
"""
import unittest

# iterative solution processes the tree level by level, assigning heights
# to a node's children.


def find_longest_consecutive_path_iterative(root):
    if root == None:
        return 0
    q = []
    q.append(root)
    root.height = 1

    max_length = 0
    while q:
        node = q.pop(0)
        max_length = max(max_length, node.height)

        for child in node.children:
            if node.data == child.data - 1:
                child.height = node.height + 1
            else:
                child.height = 1
            q.append(child)
    return max_length


# recursive solution passes in the target consecutive value to the child
# via parameters in the recursive call
def find_longest_consecutive_path_recursive(root):
    if root == None:
        return 0
    else:
        return recursive_helper(root, 0, root.data + 1)


def recursive_helper(node, curr_len, target):
    if node == None:
        return curr_len

    if node.data == target:
        curr_len += 1
    else:
        curr_len = 1

    return max(map(lambda x: recursive_helper(x, curr_len, node.data + 1), node.children if node.children else [None]))


class NaryTreeNode():

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


class TestLongestConsecutivePath(unittest.TestCase):

    def test_iterate(self):
        five = NaryTreeNode(5)
        six = NaryTreeNode(6)
        seven = NaryTreeNode(7)
        one = NaryTreeNode(1)
        two = NaryTreeNode(2)
        seven2 = NaryTreeNode(7)
        eight = NaryTreeNode(8)
        nine = NaryTreeNode(9)
        five.children.extend([six, seven, one])
        six.children.extend([two, seven2])
        seven2.add_child(eight)
        eight.add_child(nine)
        one.add_child(two)
        result = find_longest_consecutive_path_iterative(five)
        self.assertEqual(result, 5)

    def test_recursive(self):
        five = NaryTreeNode(5)
        six = NaryTreeNode(6)
        seven = NaryTreeNode(7)
        one = NaryTreeNode(1)
        two = NaryTreeNode(2)
        seven2 = NaryTreeNode(7)
        eight = NaryTreeNode(8)
        nine = NaryTreeNode(9)
        five.children.extend([six, seven, one])
        six.children.extend([two, seven2])
        seven2.add_child(eight)
        eight.add_child(nine)
        one.add_child(two)
        result = find_longest_consecutive_path_recursive(five)
        self.assertEqual(result, 5)
if __name__ == "__main__":
    unittest.main()
