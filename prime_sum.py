"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach's conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.

For the optimal solution, for every number up to n,
check if i and n-i is prime. 

O(N * 2(sqrt(N))
"""
import math
import unittest
import timeit


def find_prime_sum(n):
    for i in xrange(2, n):
        if is_prime(i) and is_prime(n - i):
            return [i, n - i]


def is_prime(n):
    if n < 2:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in xrange(2, limit):
        if n % i == 0:
            return False

    return True

print find_prime_sum(12)
"""
The slow solution generates all the primes up to n and then
proceeds to return the [a,b] where a is smallest
"""


def find_prime_sum_slow(n):
    if n < 2:
        return []
    prime_nums_dict = sieve(n)
    solution = [99999999, 99999999]
    for num, val in prime_nums_dict.iteritems():
        temp = n - num
        if prime_nums_dict.has_key(temp) and num < solution[0]:
            solution = [num, temp]
    return solution


def sieve_slow(n):
    result = {}
    N = n + 1
    arr = xrange(N)
    limit = int(math.sqrt(n)) + 1
    primes = [True] * N
    primes[0], primes[1] = False, False

    for i in xrange(2, limit):
        if primes[i]:
            j = 2
            while i * j < N:
                primes[i * j] = False
                j += 1

    for i in xrange(2, N):
        if primes[i]:
            result[arr[i]] = True
    return result


class TestPrimeSum(unittest.TestCase):

    def test_1(self):
        expect = [5, 7]
        result = find_prime_sum(12)
        self.assertEqual(expect, result)
        # timeit.timeit(find_prime_sum(50))

    def test_2(self):
        expect = [2, 2]
        result = find_prime_sum(4)
        self.assertEqual(expect, result)

    def test_3(self):
        expect = [11, 39989]
        result = find_prime_sum(40000)
        self.assertEqual(expect, result)

    def test_4(self):
        expect = [31, 16777183]
        result = find_prime_sum(16777214)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()
