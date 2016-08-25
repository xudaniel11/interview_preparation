"""
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:
Input : [(0, 0), (1, 1), (1, 2)]. X is an array of all the x values and Y is an arr of all the Y values
Output : 2
"""

import unittest


def min_steps_in_infinite_grid(X, Y):
    last_x, last_y = X[0], Y[0]
    num_steps = 0
    for i in xrange(1, len(X)):
        curr_x, curr_y = X[i], Y[i]
        steps = max(abs(curr_x - last_x), abs(curr_y - last_y))
        num_steps += steps
        last_x, last_y = curr_x, curr_y
    return num_steps


class TestMinSteps(unittest.TestCase):

    def test_case_1(self):
        X = [2, 3, 4]
        Y = [1, 4, 1]
        expected_answer = 6
        result = min_steps_in_infinite_grid(X, Y)
        self.assertEqual(result, expected_answer)

    def test_case_2(self):
        X = [2, 7, 3]
        Y = [1, 6, -2]
        expected_answer = 13
        result = min_steps_in_infinite_grid(X, Y)
        self.assertEqual(result, expected_answer)
if __name__ == "__main__":
    unittest.main()
