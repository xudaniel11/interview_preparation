"""
Find the longest consecutive path in an n-ary tree. A path is consecutive if each number is only one greater than the
one after it and one less than the one before it. Additionally, a path is a list of nodes that doesn't necessarily have to
start at the root nor end at a leaf. A path can occur in the nodes in between. Also, a path cannot go up; it only includes nodes in a sequence going downwards.

Brute force solution :( not even sure what the time complexity is here. O(3N) maybe?
"""
import unittest
import compiler.ast as compiler


def consecutive_path_nary_tree(root):
    if root == None:
        return 0
    paths = []
    paths.extend(make_paths(root))
    possible_paths = []
    for path in paths:
        possible_paths.append(compiler.flatten(path))
    consecutive_paths = get_consecutive_paths(possible_paths)
    return max(consecutive_paths, key=len) if consecutive_paths else []


def make_paths(node):
    paths = []
    if not node:
        return []
    if not (node.children):
        print "hit leaf"
        return node.val
    print "curr node: " + str(node.val)
    for val in node.val:
        # print "curr val: " + str(val)
        for child in node.children:
            for child_val in make_paths(child):
                # print "child: " + str(child.val), "grandchild: " +
                # str(child_val)
                if child_val == None:
                    continue
                temp = [val]
                temp.extend([child_val])
                paths.extend([temp])
    # print paths
    compiler.flatten(paths)
    return paths


def get_consecutive_paths(paths):
    result = []
    for path in paths:
        bools = all(x == y - 1 for x, y in zip(path, path[1:]))
        if bools:
            result.append(path)
    return result


class NaryTreeNode():

    def __init__(self, val, N):
        self.N = N
        self.val = val
        self.children = None


class TestConsecutivePath(unittest.TestCase):

    def test_case_1(self):
        a = NaryTreeNode([3, 4], 3)
        b = NaryTreeNode([1, 7], 3)
        c = NaryTreeNode([4, 6], 3)
        d = NaryTreeNode([9, 8], 3)
        e = NaryTreeNode([3, 2], 3)
        f = NaryTreeNode([5, 6], 3)
        g = NaryTreeNode([5, 3], 3)
        h = NaryTreeNode([2, 1], 3)
        i = NaryTreeNode([6, None], 3)
        j = NaryTreeNode([6, None], 3)
        a.children = [b, c, d]
        b.children = [e, f, None]
        c.children = [g, h, None]
        g.children = [i, j, None]
        result = consecutive_path_nary_tree(a)
        print result
        self.assertEqual(result, [3, 4, 5, 6])

    def test_case_2(self):
        a = NaryTreeNode([3, 4], 3)
        b = NaryTreeNode([4, 7], 3)
        c = NaryTreeNode([4, 6], 3)
        d = NaryTreeNode([9, 8], 3)
        e = NaryTreeNode([5, 2], 3)
        f = NaryTreeNode([5, 6], 3)
        g = NaryTreeNode([6, 1], 3)
        h = NaryTreeNode([3, 7], 3)
        a.children = [b, c, d]
        b.children = [e, f, None]
        e.children = [g, None, None]
        g.children = [h, None, None]
        result = consecutive_path_nary_tree(a)
        print result, "\n"
        self.assertEqual(result, [3, 4, 5, 6, 7])

    def test_case_3(self):
        a = NaryTreeNode([3, 4], 3)
        b = NaryTreeNode([1, 7], 3)
        d = NaryTreeNode([9, 8], 3)
        e = NaryTreeNode([3, 2], 3)
        f = NaryTreeNode([5, 6], 3)
        a.children = [b, None, d]
        b.children = [e, f, None]
        result = consecutive_path_nary_tree(a)
        print result
        self.assertEqual(result, [])

    def test_case_4(self):
        a = NaryTreeNode([3, 4], 3)
        b = NaryTreeNode([4, 7], 3)
        c = NaryTreeNode([1, 5], 3)
        a.children = [b, None, None]
        b.children = [c, None, None]
        result = consecutive_path_nary_tree(a)
        self.assertEqual(result, [3, 4, 5])
if __name__ == "__main__":
    unittest.main()
