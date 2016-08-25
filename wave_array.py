"""
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

E.g. Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
 NOTE : If there are multiple answers possible, return the one thats lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3]
"""
import unittest


def wave_array(arr):
    arr.sort()
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


class TestWaveArray(unittest.TestCase):

    def test_1(self):
        a = [1, 2, 3, 4]
        result = wave_array(a)
        expected = [2, 1, 4, 3]
        self.assertEqual(result, expected)

    def test_2(self):
        a = [14, 5, 14, 34, 42, 63, 17, 25, 39,
             61, 97, 55, 33, 96, 62, 32, 98, 77, 35]
        result = wave_array(a)
        expected = [14, 5, 17, 14, 32, 25, 34, 33, 39,
                    35, 55, 42, 62, 61, 77, 63, 97, 96, 98]
        # expected = [14, 5, 25, 17, 34, 33, 42, 39, 61, 55, 63, 62, 97, 96]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
