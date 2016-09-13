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

"""O(N^2) solution"""


def trapping_rain_water(arr):
    result = 0
    for i, bar_height in enumerate(arr):
        if i == 0:
            left = 0
            right = max(arr[i + 1:])
        elif i == len(arr) - 1:
            right = 0
            left = max(arr[:i])
        else:
            right = max(arr[i + 1:])
            left = max(arr[:i])
        height = min(left, right)
        tmp = height - bar_height if height >= bar_height else 0
        # print tmp
        result += tmp
    return result


a0 = [2, 1, 4, 3, 1, 0, 3]
print "should be 6: is {}".format(trapping_rain_water(a0))
a1 = [3, 0, 0, 2, 0, 4]
print "should be 10: is {}".format(trapping_rain_water(a1))
a2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print "should be 6: is {}".format(trapping_rain_water(a2))
