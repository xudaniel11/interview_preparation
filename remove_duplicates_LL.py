"""
Remove duplicates from an unsorted linked list in O(1) space.
"""
import Singly_LL as LL
import unittest


def remove_duplicates(ll):
    if ll.get_size() == 0 or ll.get_size == 1:
        return ll

    prev = ll.head
    curr = ll.head.next
    while curr:
        runner = ll.head
        while runner != curr:
            if runner.val == curr.val:
                # keep the first duplicate and remove curr, which is the
                # later one
                temp = curr.next
                prev.next = temp
                curr = temp
                break
            runner = runner.next
        if runner == curr:
            # only move on to the next curr if we've finished removing all
            # the dupes
            prev = curr
            curr = curr.next
    return ll


class TestRemoveDupes(unittest.TestCase):

    def test_1(self):
        example = LL.Singly_LL()
        example.add(3)
        example.add(1)
        example.add(2)
        example.add(2)
        example.add(4)
        result = remove_duplicates(example)
        result.print_LL()  # should 3 1 2 4
        print "\n"

    def test_2(self):
        example = LL.Singly_LL()
        example.add(2)
        example.add(1)
        example.add(2)
        example.add(2)
        result = remove_duplicates(example)
        result.print_LL()  # should be 2

if __name__ == "__main__":
    unittest.main()
