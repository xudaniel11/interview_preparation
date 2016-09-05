"""
0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight
how to pick items to pick items from this set to maximize sum of value of items such that
sum of weights is less than or equal to maximum allowed weight.
"""
import numpy as np
# np.set_printoptions(threshold=np.inf)
import unittest


def knapsack(bag_items, weight):
    n, m = len(bag_items) + 1, weight + 1
    mat = np.zeros((n, m))

    for i in xrange(1, n):
        obj, obj_value, obj_weight = bag_items[i - 1]
        for j in xrange(1, m):
            curr_weight = j
            if curr_weight >= obj_weight:
                val_including = obj_value + \
                    mat[i - 1, curr_weight - obj_weight]
                val_excluding = mat[i - 1, j]
                mat[i, j] = max(val_including, val_excluding)
            else:
                mat[i, j] = mat[i - 1, j]

    result = []
    w = weight
    for i in reversed(xrange(1, n)):
        was_added = mat[i, w] != mat[i - 1, w]
        if was_added:
            obj_name, obj_value, obj_weight = bag_items[i - 1]
            result.append(bag_items[i - 1])
            w -= obj_weight

    max_val = sum(map(lambda x: x[1], result))
    max_weight = sum(map(lambda x: x[2], result))

    return max_val, max_weight


class TestKnapsack(unittest.TestCase):

    def test_1(self):
        items = [['obj0', 1, 2], ['obj1', 5, 3], ['obj2', 6, 5]]
        result = knapsack(items, 7)
        expected = 7, 7  # max weight, max val
        self.assertEqual(result, expected)

    def test_2(self):
        items = [['socks', 50, 4], ['sunglasses', 20, 7], ['map', 150, 9], ['suntan cream', 70, 11], ['compass', 35, 13], ['glucose', 60, 15], ['towel', 12, 18], ['note-case', 80, 22], ['cheese', 30, 23], ['t-shirt', 15, 24], ['banana', 60, 27],
                 ['book', 10, 30], ['camera', 30, 32], ['apple', 40, 39], ['waterproof trousers', 70, 42], ['waterproof overclothes', 75, 43], ['trousers', 10, 48], ['sandwich', 160, 50], ['beer', 10, 52], ['tin', 45, 68], ['umbrella', 40, 73], ['water', 200, 153]]
        result = knapsack(items, 400)
        expected = 1030, 396  # max value, # max weight <= 400
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
