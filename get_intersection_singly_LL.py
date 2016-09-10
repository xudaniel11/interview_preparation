"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


A:          a1 -> a2
                   \
                     c1 -> c2 -> c3
                   /
B:     b1 -> b2 -> b3

begin to intersect at node c1.

 Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Solution: find difference in length of the two input lists. Then start at the 
difference-eth node in the longer list. That way, it will seem like the two lists
are of equal length when we iterate through them. 

Time: O(M+N)
Space: O(1)
"""
import unittest


def get_intersection(list1head, list2head):
    difference = abs(list1head.get_size() - list2head.get_size())
    longer_list_head = list1head if list1head.get_size(
    ) > list2head.get_size() else list2head
    shorter_list_head = list2head if list2head.get_size() < list1head.get_size() else list1

    longer_curr = longer_list_head
    for i in range(difference):
        longer_curr = longer_curr.next

    shorter_curr = shorter_list_head
    while longer_curr:
        if longer_curr == shorter_curr:
            return longer_curr.val
        longer_curr = longer_curr.next
        shorter_curr = shorter_curr.next

    return -1


class Singly_LL_Node():

    def __init__(self, val):
        self.val = val
        self.next = None

    def get_size(self):
        """Takes a node and outputs how many nodes there are after it."""
        curr = self
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count


class TestGetIntersection(unittest.TestCase):

    def test_1(self):
        head1 = Singly_LL_Node(1)
        head1.next = Singly_LL_Node(2)
        head1.next.next = Singly_LL_Node(3)
        head1.next.next.next = Singly_LL_Node(4)
        head1.next.next.next.next = Singly_LL_Node(5)

        head2 = Singly_LL_Node(6)
        head2.next = Singly_LL_Node(7)
        head2.next.next = head1.next.next.next
        result = get_intersection(head1, head2)
        self.assertEqual(result, 4)

    def test_2(self):
        head1 = Singly_LL_Node(1)
        head1.next = Singly_LL_Node(2)
        head1.next.next = Singly_LL_Node(3)
        head1.next.next.next = Singly_LL_Node(4)
        head1.next.next.next.next = Singly_LL_Node(5)

        head2 = Singly_LL_Node(6)
        head2.next = Singly_LL_Node(7)
        result = get_intersection(head1, head2)
        self.assertEqual(result, -1)

    def test_3(self):
        head2 = Singly_LL_Node(1)
        head1 = Singly_LL_Node(2)
        head2.next = head1

        result = get_intersection(head2, head1)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
