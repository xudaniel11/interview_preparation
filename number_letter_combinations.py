"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

You don't have to return all the mappings, only the number of valid mappings.

Follow up harder question: return all the mappings LOL
"""
import unittest

# initial solution doesn't take into account the fact that '0' doesn't
# have a letter mapping


def number_letter_combinations_WRONG(input_str):
    cache = [1, 1]

    for i in range(1, len(input_str)):
        if int(input_str[i - 1] + input_str[i]) < 27:
            cache.append(int(cache[i]) + int(cache[i - 1]))
        else:
            cache.append(int(cache[i]))
    return cache[-1]


def number_letter_combinations(input_str):
    n = len(input_str) + 1
    # edge case when there are many 0's in the input. again, 0 doesn't correspond to
    # an alphabet letter
    if all(x == '0' for x in input_str) or input_str[0] == '0' or '00' in input_str:
        return 0
    if len(input_str) == 1:
        return 1

    count = [0] * n
    # base case
    count[0] = 1
    count[1] = 1

    for i in range(2, n):
        if input_str[i - 1] > '0':
            count[i] = count[i - 1]
        # if we see a 0 reset our count to a prev amount
        if input_str[i - 2] == '1' or (input_str[i - 2] == '2' and input_str[i - 1] < '7'):
            count[i] += count[i - 2]
    print count
    return count[-1]

print number_letter_combinations(raw_input())


class TestNumberLetterCombinations(unittest.TestCase):

    def test_case_1(self):
        input_str = "0"
        result = number_letter_combinations(input_str)
        self.assertEqual(result, 0)

    def test_case_2(self):
        input_str = "1212"
        result = number_letter_combinations(input_str)
        self.assertEqual(result, 5)

    def test_case_3(self):
        input_str = "5163490394499093221199401898020270545859326357520618953580237168826696965537789565062429676962877038781708385575876312877941367557410101383684194057405018861234394660905712238428675120866930196204792703765204322329401298924190"
        result = number_letter_combinations(input_str)
        self.assertEqual(result, 0)

    def test_case_4(self):
        input_str = "8"
        result = number_letter_combinations(input_str)
        self.assertEqual(result, 1)

    def test_case_5(self):
        input_str = "32925665678138257423442343752148360796465852883409126159293254159974370974059818198867156827877059067081419274873853679038"
        result = number_letter_combinations(input_str)
        self.assertEqual(result, 0)
if __name__ == '__main__':
    unittest.main()
