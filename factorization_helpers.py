"""
Given a number N, find all factors of N.

E.g. if N = 6, result factors = {1, 2, 3, 6}

Ensure the returned array is sorted.
"""
import math
import unittest


def get_factors(n):
    limit = int(math.sqrt(n))
    result = []
    for i in range(1, limit + 1):
        if n % i == 0:
            result.append(i)
            if i != limit:
                result.append(n / i)
    return sorted(result)


"""
Given a number N, verify if N is prime or not.
"""


def verify_prime(n):
    if n <= 1:
        return False
    limit = int(math.sqrt(n))
    result = True
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return result


"""
Given a number N, find all prime numbers upto N ( N included ).

Example:

if N = 7,

all primes till 7 = {2, 3, 5, 7}

Make sure the returned array is sorted.
"""


def sieve_of_eratosthenes(n):
    arr = range(n + 1)
    N = len(arr)
    limit = int(math.sqrt(N))
    prime_list = [True] * N
    prime_list[0], prime_list[1] = False, False

    for i in range(2, limit + 1):
        if prime_list[i]:
            j = 2
            while i * j < N:
                prime_list[i * j] = False
                j += 1

    result = []
    for i in range(2, N):
        if prime_list[i]:
            result.append(arr[i])
    return result


class TestFactorization(unittest.TestCase):

    def test_sieve(self):
        result = sieve_of_eratosthenes(50)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(result, expected)

    def test_get_factors(self):
        result = get_factors(36)
        expected = [1, 2, 3, 4, 6, 9, 12, 18, 36]
        self.assertEqual(result, expected)

    def test_verify_prime(self):
        result = verify_prime(7)
        self.assertEqual(result, True)
if __name__ == "__main__":
    unittest.main()
