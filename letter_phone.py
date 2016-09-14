"""
Given a digit string, return all possible letter combinations that the
number could represent.

Digits are mapped to letters just like on the telephone buttons.

The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
"""
import unittest


def letter_phone(s):
    number_map = {'1': ['1'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': ['0']
                  }

    if len(s) == 1:
        return number_map[s]
    children = letter_phone(s[1:])
    result = []
    curr = number_map[s[0]]
    for letter in curr:
        for child in children:
            result.append(letter + child)
    return result


class TestLetterPhone(unittest.TestCase):

    def test_1(self):
        result = letter_phone("23")
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(result, expected)

    def test_2(self):
        result = letter_phone("256")
        expected = ['ajm', 'ajn', 'ajo', 'akm', 'akn', 'ako', 'alm', 'aln', 'alo', 'bjm', 'bjn', 'bjo', 'bkm',
                    'bkn', 'bko', 'blm', 'bln', 'blo', 'cjm', 'cjn', 'cjo', 'ckm', 'ckn', 'cko', 'clm', 'cln', 'clo']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
