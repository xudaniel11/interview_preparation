"""
Given n non-negative integers representing the histogram's bar height
where the width of each bar is 1, find the area of largest rectangle
in the histogram.
"""
import unittest


def naive_largest_rectangle(histogram):
    n = len(histogram)
    possibilities = []
    for i in range(n):
        start = i
        start_block = histogram[start]
        end = i
        for j in range(i + 1, n):
            if histogram[j] < start_block:
                break
            end = j
        length = (end - start) + 1
        possibilities.append(start_block * length)
    return max(possibilities)


def largest_rectangle(histogram):
    stack = [0]
    max_area = -1
    for i in range(len(histogram)):
        if not stack or histogram[i] >= histogram[stack[-1]]:
            stack.append(i)
        elif histogram[i] < histogram[stack[-1]]:
            top = 0
            while stack and histogram[i] < histogram:
                top = stack.pop()
                if not stack:
                    area = histogram[top] * i
                else:
                    area = histogram[top] * (i - stack[-1] - 1)
                max_area = max(max_area, area)
                top = stack.pop()

    return max_area


class TestLargestRectangle(unittest.TestCase):

    # def test_1(self):
        # a = [90, 58, 69, 70, 82, 100, 13, 57, 47, 18]
        # result = largest_rectangle(a)
        # expected = 348
        # self.assertEqual(result, expected)

    def test_2(self):
        a = [1, 2, 4, 2, 1, 3]
        result = largest_rectangle(a)
        expected = 6
        self.assertEqual(result, expected)

    # def test_3(self):
    #     a = [2, 2, 2, 6, 1, 5, 4, 2, 2, 2, 2]
    #     result = largest_rectangle(a)
    #     expected = 12
    #     self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()
