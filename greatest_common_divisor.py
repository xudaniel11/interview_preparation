"""
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
"""
import unittest


def gcd(m, n):
    m_divisors = get_divisors(m)
    n_divisors = get_divisors(n)
    in_common = set(m_divisors).intersection(n_divisors)
    if in_common:
        return max(in_common)
    else:
        return max(m_divisors + n_divisors)


def get_divisors(x):
    limit = int(x**(0.5)) + 1
    result = []
    for i in xrange(1, limit):
        if x % i == 0:
            result.extend([i, x / i])
    return result if result else [x]


class TestGCD(unittest.TestCase):

    def test_1(self):
        expect = 1
        result = gcd(1, 0)
        self.assertEqual(expect, result)
        # timeit.timeit(find_prime_sum(50))

    def test_2(self):
        expect = 2
        result = gcd(2, 0)
        self.assertEqual(expect, result)

    def test_3(self):
        expect = 1
        result = gcd(3, 4)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()
