"""
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False
"""


def is_palindromic(n):
    if n < 0:
        return False
    str_n = str(n)
    for i in range(len(str_n) / 2):
        if str_n[i] != str_n[len(str_n) - i - 1]:
            return False
    return True

print is_palindromic(12121)  # True
print is_palindromic(123)  # True
print is_palindromic(-1)  # False
print is_palindromic(0)  # True
