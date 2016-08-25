"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""
import unittest

# shitty solution


def shitty_merge_intervals(arr, interval):
    result = [arr[0]]
    merged = False
    N = len(arr)
    count = 1
    while count < N:
        next = arr[count]
        curr = result[-1]
        if not merged:
            if mergeable(result[-1], interval):
                merged_int = merge(result[-1], interval)
                result[-1] = merged_int
                merged = True
            elif mergeable(result[-1], next):
                merged_int = merge(result[-1], next)
                result[-1] = merged_int
                count += 1
            else:
                result.append(next)
                count += 1
        else:
            if mergeable(result[-1], next):
                merged_int = merge(result[-1], next)
                result[-1] = merged_int
                count += 1
            else:
                result.append(next)
                count += 1
    if not merged:
        merged_int = merge(result[-1], interval)
        result[-1] = merged_int
    return result


def mergeable(intr0, intr1):
    if intr1[0] >= intr0[0] and intr1[0] <= intr0[1]:
        return True
    else:
        return False


def merge(intr0, intr1):
    result = [min(intr0[0], intr1[0]), max(intr0[1], intr1[1])]
    return result

# better solution ripped from http://www.cnblogs.com/zuoyuan/p/3782048.html


class Interval:

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge_intervals(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x.start)
    length = len(intervals)
    result = []
    for i in range(length):
        if not result:
            result.append(intervals[i])
        else:
            if result[-1].start <= intervals[i].start <= result[-1].end:
                result[-1].end = max(intervals[i].end, result[-1].end)
            else:
                result.append(intervals[i])
    return result


class TestMergeIntervals(unittest.TestCase):

    def test_1(self):
        a = [Interval(1, 3), Interval(6, 9)]  # [[1, 3], [6, 9]]
        insert = Interval(2, 5)  # [2, 5]
        result = merge_intervals(a, insert)
        for each in result:
            # expected [[1, 5], [6, 9]] or Interval(1, 5), Interval(6, 9)]
            print each.start, each.end

    def test_shitty_2(self):
        a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        insert = [4, 9]
        result = shitty_merge_intervals(a, insert)
        expected = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(result, expected)

    def test_shitty_3(self):
        a = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        insert = [6, 10]
        result = shitty_merge_intervals(a, insert)
        expected = [[1, 10]]
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()
