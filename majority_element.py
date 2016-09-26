"""
Given array of positive ints, return the majority element (strict majority: more than half)
input [4, 4, 5, 5] would return -1
[1] -> 1
[4, 4, 5, 5, 4] -> 4
[6, 5, 5, 5, 5, 5, 5, 3, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6] -> 6

Moore's Voting Algorithm -- if we cancel out each occurence of a candidate element
with all the other elements that are different from that candidate, then that candidate
will exist until the end if its a majority element.

O(N) time, O(1) space

https://www.quora.com/What-is-the-proof-of-correctness-of-Moores-voting-algorithm#
"""
import unittest


def num_occurences(arr):
    candidate = None
    votes_for = 0
    votes_against = 0
    for num in arr:
        if candidate == None:
            candidate = num

        if num == candidate:
            votes_for += 1
        elif num != candidate:
            votes_against += 1

        if votes_for == votes_against:
            candidate = None
            votes_for = 0
            votes_against = 0

    if arr.count(candidate) > len(arr) / 2:
        return candidate
    else:
        return -1


class TestMajorityElement(unittest.TestCase):

    def test_1(self):
        ex = [2, 2, 3, 5, 2, 2, 6]
        result = num_occurences(ex)
        self.assertEqual(result, 2)

    def test_2(self):
        ex = [3, 3, 4, 2, 4, 4, 2, 4, 4]
        result = num_occurences(ex)
        self.assertEqual(result, 4)

    def test_3(self):
        ex = [3, 3, 4, 2, 4, 4, 2, 4]
        result = num_occurences(ex)
        self.assertEqual(result, -1)

    def test_4(self):
        self.assertEqual(num_occurences([1]), 1)
if __name__ == "__main__":
    unittest.main()
