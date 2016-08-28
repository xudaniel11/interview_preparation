"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

"""
import unittest
import itertools as it


def largest_number_WRONG_SOLUTION(arr):  # takes waaaay too long: O(len(arr)!)
    max_so_far = -999999
    for tup in it.permutations(arr, len(arr)):
        permutation = int(''.join(str(num) for num in tup))
        max_so_far = max(max_so_far, permutation)
    return str(max_so_far)


"""
The correct solution
"""


def compare(X, Y):
    # print X, Y
    X, Y = str(X), str(Y)
    XY = X + Y
    YX = Y + X
    if XY == YX:
        return 0
    elif XY < YX:
        return -1
    elif XY > YX:
        return 1


def largest_number(arr):
    arr.sort(cmp=compare, reverse=True)
    # print arr
    result = ''.join(str(x) for x in arr)
    if int(result) == 0:
        return str(0)
    else:
        return result


class TestLargestNumber(unittest.TestCase):

    def test_1(self):
        print "aoiwejf"
        a = [3, 30, 34, 5, 9]
        answer = '9534330'
        result = largest_number(a)
        self.assertEqual(answer, result)

    def test_2(self):
        print "aoijw"
        a = [472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412]
        answer = '9648527226766636354854724412368319'
        result = largest_number(a)
        self.assertEqual(answer, result)

    def test_3(self):
        print "aoiwejf"
        a = [0, 0, 0, 0, 0]
        answer = '0'
        result = largest_number(a)
        self.assertEqual(answer, result)
if __name__ == "__main__":
    unittest.main()
