"""
Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
The answer would be 'a'
"""
import unittest


def longest_common_prefix(arr):
    result = ""
    if not arr:
        return result

    length_of_shortest = min(list(map(lambda x: len(x), arr)))
    for i in xrange(length_of_shortest):
        ith_chars = list(map(lambda x: x[i], arr))
        ith_char = ith_chars[0]
        if all(x == ith_char for x in ith_chars):
            result += ith_char
        else:
            return result
    return result


class TestLongestCommonPrefix(unittest.TestCase):

    def test_1(self):
        a = [
            "abcdefgh",
            "aefghijk",
            "abcefgh"]
        result = longest_common_prefix(a)
        expected = 'a'
        self.assertEqual(result, expected)

    def test_2(self):
        b = [
            "abcdef",
            "abcde",
            "abc"]
        result = longest_common_prefix(b)
        expected = 'abc'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
