"""
Find the distance between the two closest elements in an array of numbers.
"""
import unittest


def get_distance(arr):
    if len(arr) < 2:
        return 0

    arr = sorted(arr)
    min_distance = abs(arr[0] - arr[1])
    indices = [0, 1]

    for i in range(1, len(arr) - 1):
        curr = arr[i]
        next = arr[i + 1]
        dist = abs(curr - next)
        # print curr, next, dist, min_distance
        if dist < min_distance:
            min_distance = dist
            indices = [curr, next]
    return abs(indices[0] - indices[1])


class TestLargestDistance(unittest.TestCase):

    def test_1(self):
        a = [5, 0, -1, 6.5, 3]
        result = get_distance(a)
        expect = 1
        self.assertEqual(result, expect)

    def test_2(self):
        a = []
        result = get_distance(a)
        expect = 0
        self.assertEqual(result, expect)

    def test_3(self):
        a = [1]
        result = get_distance(a)
        expect = 0
        self.assertEqual(result, expect)

    def test_4(self):
        a = [1, 1000, 3, -5]
        result = get_distance(a)
        expect = 2
        self.assertEqual(result, expect)

if __name__ == "__main__":
    unittest.main()
