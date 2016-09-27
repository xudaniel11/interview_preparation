"""
Print all the consecutive paths in an N-ary tree. A path doesn't have to start
at root nor end at leaf, but its sequence has to be consecutive.
For example, 1 -> 2 -> 6 is not a consecutive path, but 1 -> 2 -> 3 is.
"""
import unittest


def find_consecutive_paths(root):
    if root == None:
        return
    depth = get_depth(root)
    path = [None] * depth
    get_consecutive_paths(root, path, 0)


def get_consecutive_paths(node, path, level):
    if node == None:
        return
    path[level] = node.data

    for i in reversed(range(level + 1)):
        if len(filter(lambda x: x is not None, path)) == 1 or i == 0:
            break
        else:
            print path, path[i]
            if path[i] != path[i - 1] + 1:
                break
            else:
                print_path(path, i - 1, level)
    return map(lambda x: get_consecutive_paths(x, path, level + 1), node.children)


def print_path(path, start, end):
    for i in range(start, end + 1):
        print path[i],
    print "\n"


def get_depth(node):
    if node == None:
        return 0
    elif not node.children:
        return 1
    else:
        return 1 + max(list(map(lambda x: get_depth(x), node.children)))


class NaryTreeNode():

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


class TestConsecutivePaths(unittest.TestCase):

    def test_1(self):
        five = NaryTreeNode(5)
        six = NaryTreeNode(6)
        seven = NaryTreeNode(7)
        one = NaryTreeNode(1)
        two = NaryTreeNode(2)
        seven2 = NaryTreeNode(7)
        eight = NaryTreeNode(8)
        three = NaryTreeNode(3)
        five.children.extend([six, seven, one])
        six.children.extend([two, seven2, eight])
        one.add_child(three)
        find_consecutive_paths(five)


if __name__ == "__main__":
    unittest.main()
