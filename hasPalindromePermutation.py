"""
Write an efficient function that checks whether any permutation of an input string is a palindrome.
Examples:

"civic" should return True
"ivicc" should return True
"livci" should return False
"civil" should return False

Solution: make a set to keep track of a letters that match. 
Iterate through string, adding to set if it hasn't yet been seen. Remove from set if seen.
Return true if no more than one of the characters appears an odd numbers of times.

Time: O(N)
Space: O(k) where k is the number of unique characters, or ~O(1)
"""


def hasPalindromePermutation(s):
    unpairedCharacters = set()

    for index, char in enumerate(s):
        if char in unpairedCharacters:
            unpairedCharacters.remove(char)
        else:
            unpairedCharacters.add(char)
    return False if len(unpairedCharacters) > 1 else True

a0 = "civic"
print "Should be true: {}".format(hasPalindromePermutation(a0))
a1 = "ivicc"
print "Should be true: {}".format(hasPalindromePermutation(a1))
a2 = "livci"
print "Should be false: {}".format(hasPalindromePermutation(a2))
a3 = "civil"
print "Should be false: {}".format(hasPalindromePermutation(a3))
