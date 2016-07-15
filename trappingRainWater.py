"""
Given N non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Time analysis: O(N).
"""


def trappingRainWater(arr):
    left, right = [arr[0]], arr[:]
    result = 0
    for i, num in enumerate(arr):
        if i == 0:
            continue
        else:
            left.append(max(num, max(arr[:i + 1])))
    backwards = range(len(arr))
    backwards.reverse()
    for i in backwards:
        if i == len(arr) - 1:
            continue
        else:
            right[i] = max(arr[i], right[i + 1])

    for i, height in enumerate(arr):
        minValue = min(left[i], right[i])
        result += minValue - height
    return result

a0 = [2, 1, 4, 3, 1, 0, 3]
print "should be 6: is {}".format(trappingRainWater(a0))
a1 = [3, 0, 0, 2, 0, 4]
print "should be 10: is {}".format(trappingRainWater(a1))
