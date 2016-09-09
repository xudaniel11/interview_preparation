"""
Given to sorted lists with unique elements, merge them and removed duplicates.

E.g.:
INPUT
list_1 = [1, 4, 5, 6]
list_2 = [1, 2, 3, 7]

OUTPUT
[1,2,3,4,5,6,7]

"""
import unittest


def merge(list1, list2):
    result = []

    if not list1 or not list2:
        return result

    seen = {}
    counter_list1 = 0
    counter_list2 = 0
    while counter_list1 < len(list1) and counter_list2 < len(list2):
        if list1[counter_list1] < list2[counter_list2]:
            smaller_elem = list1[counter_list1]
            counter_list1 += 1
        elif list1[counter_list1] > list2[counter_list2]:
            smaller_elem = list2[counter_list2]
            counter_list2 += 1
        else:
            smaller_elem = list1[counter_list1]
            counter_list1 += 1
            counter_list2 += 1

        if smaller_elem in seen:
            continue
        else:
            result.append(smaller_elem)
            seen[smaller_elem] = True

    shorter_list = list1 if len(list1) <= len(list2) else list2
    if counter_list1 >= len(shorter_list):
        longest_list = list2
        subarr_counter = counter_list2
    elif counter_list2 >= len(shorter_list):
        longest_list = list1
        subarr_counter = counter_list1

    subarr = longest_list[subarr_counter:len(longest_list)]
    for i, num in enumerate(subarr):
        if num in seen:
            continue
        else:
            result.append(num)
            seen[num] = True

    return result


class TestMergeSortedLists(unittest.TestCase):

    def test_1(self):
        list1 = [1, 4, 5, 6]
        list2 = [1, 2, 3, 7]
        result = merge(list1, list2)
        expected = range(1, 8)
        self.assertEqual(result, expected)

    def test_2(self):
        list1 = [1, 4, 5]
        list2 = [1, 2, 3, 7, 9, 10]
        result = merge(list1, list2)
        expected = [1, 2, 3, 4, 5, 7, 9, 10]
        self.assertEqual(result, expected)

    def test_3(self):
        list1 = [1]
        list2 = [1]
        result = merge(list1, list2)
        expected = [1]
        self.assertEqual(result, expected)

    def test_4(self):
        list1 = []
        list2 = [1]
        result = merge(list1, list2)
        expected = []
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()
