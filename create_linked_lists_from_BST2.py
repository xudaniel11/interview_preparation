import unittest


def depth_LL(node):
    headLL = LinkedList()
    headLL.add(node)
    level = 0
    result = [(level, headLL)]
    while True:
        curr_level, ll = result[level]
        new_LL = LinkedList()
        curr_llnode = ll.head
        while curr_llnode:
            BTnode = curr_llnode.BTnode
            if BTnode.left:
                new_LL.add(BTnode.left)
            if BTnode.right:
                new_LL.add(BTnode.right)
            curr_llnode = curr_llnode.next
        if new_LL.size == 0:
            break
        level += 1
        result.append((level, new_LL))
    return result


class LinkedListNode():

    def __init__(self, node):
        self.BTnode = node
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, node):
        if self.head == None:
            self.head = LinkedListNode(node)
            self.tail = self.head
        else:
            new_tail = LinkedListNode(node)
            self.tail.next = new_tail
            self.tail = new_tail

        self.size += 1

    def list(self):
        return self.lst

    def size(self):
        return self.size

    def printLL(self):
        curr = self.head
        while curr:
            print curr.BTnode.val,
            curr = curr.next


class BinaryTreeNode():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Test_Create_LL_from_BST(unittest.TestCase):

    def test_case_1(self):
        root = BinaryTreeNode('A')
        root.left = BinaryTreeNode('B')
        root.right = BinaryTreeNode('C')
        root.right.left = BinaryTreeNode('F')
        root.right.right = BinaryTreeNode('G')
        root.left.left = BinaryTreeNode('D')
        root.left.right = BinaryTreeNode('E')
        result = depth_LL(root)
        for tup in result:
            level, ll = tup
            print level, ll.printLL()


if __name__ == "__main__":
    unittest.main()
