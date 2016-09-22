"""
Given n non-negative integers representing the histogram's bar height
where the width of each bar is 1, find the area of largest rectangle
in the histogram.
"""
"""
Given n non-negative integers representing the histogram’s bar height
where the width of each bar is 1, find the area of largest rectangle
in the histogram.
"""
import unittest


def largest_rectangle(bar_heights):
    stack = []
    max_area = -1
    i = 0
    histogram = bar_heights[:]
    histogram.append(0)
    limit = len(histogram)
    while i < limit:
        if not stack or histogram[i] >= histogram[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if not stack:
                area = histogram[top] * i
            else:
                area = histogram[top] * (i - stack[-1] - 1)
            max_area = max(max_area, area)
    return max_area


class TestLargestRectangle(unittest.TestCase):

    def test_1(self):
        a = [90, 58, 69, 70, 82, 100, 13, 57, 47, 18]
        result = largest_rectangle(a)
        expected = 348
        self.assertEqual(result, expected)

    def test_2(self):
        a = [1, 2, 4, 2, 1, 3]
        result = largest_rectangle(a)
        expected = 6
        self.assertEqual(result, expected)

    def test_3(self):
        a = [2, 2, 2, 6, 1, 5, 4, 2, 2, 2]
        result = largest_rectangle(a)
        expected = 10
        self.assertEqual(result, expected)

    def test_4(self):
        a = [1, 2, 0, 5, 4, 3]
        result = largest_rectangle(a)
        expected = 9
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()
