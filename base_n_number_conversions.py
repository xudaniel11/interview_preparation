"""
Given a number N >= 0, find its representation in binary.

Example:

if N = 6,

binary form = 110
"""
import unittest


def dec_to_bin(n):
    if not n:
        return '0'
    num = n
    result = ""
    while num > 0:
        if num == 1:
            result += str(1)
            break
        quotient = num / 2
        remainder = num % 2
        result += str(remainder)
        num = quotient
    return result[::-1] if result else '0'


def bin_to_dec(s):
    result = 0
    s = s[::-1]
    for i, num in enumerate(s):
        if int(num) == 1:
            result += 2**i
    return result

"""
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1

    B -> 2

    C -> 3

    ...

    Z -> 26

    AA -> 27

    AB -> 28
"""


def column_number(s):
    s = s.lower()
    letters = list(map(chr, range(96, 123)))
    result = 0
    for i, num in enumerate(s[::-1]):
        result += (26 ** i) * letters.index(num)
    return result


class TestBaseN(unittest.TestCase):

    def test_dec_to_bin_1(self):
        expect = "1010"
        result = dec_to_bin(10)
        self.assertEqual(expect, result)

    def test_dec_to_bin2(self):
        expect = "0"
        result = dec_to_bin(0)
        self.assertEqual(expect, result)

    def test_dec_to_bin_3(self):
        expect = "0"
        result = dec_to_bin(None)
        self.assertEqual(expect, result)

    def test_bin_to_dec_1(self):
        expect = 10
        result = bin_to_dec('1010')
        self.assertEqual(expect, result)

    def test_bin_to_dec_2(self):
        expect = 0
        result = bin_to_dec('0')
        self.assertEqual(expect, result)

    def test_col_num_1(self):
        expect = 731
        result = column_number('ABC')
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()
