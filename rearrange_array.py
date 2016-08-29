"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
* All elements in the array are in the range [0, N-1]
* N * N does not overflow for a signed integer 

solution taken from https://github.com/interviewcoder/interviewbit/blob/master/s02.math/_08_Rearrange/Solution.java
bc idk how to do this question using only a constant amount of space
"""
import unittest


def rearrange(arr):
    N = len(arr)
    for i in range(N):
        x = arr[i]
        y = arr[x]
        if y >= N:
            y = arr[x] % N
        encode = x + y * N
        arr[i] = encode

    for i in range(N):
        arr[i] = arr[i] / N
    return arr


class TestRearrange(unittest.TestCase):

    def test_1(self):
        result = rearrange([6, 1, 0, 2, 3, 5, 4])
        expected = [4, 1, 6, 0, 2, 5, 3]
        self.assertEqual(result, expected)

        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()
