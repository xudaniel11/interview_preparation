"""
"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
finds the corresponding closing parenthesis. For example, Example: if the example string above is input with the number 10
(position of the first parenthesis), the output should be 79 (position of the last parenthesis).

Solution: keep track of how many open parens there are, and decrement when we see a close paren accordingly.
Time: O(N)
Space: O(1)
"""


def matchingParens(s):
    numOpenParens = 0
    for index, char in enumerate(s):
        if char == ')' and (numOpenParens == 1):
            numOpenParens -= 1
            return index
        elif char == '(':
            numOpenParens += 1
        elif char == ')':
            numOpenParens -= 1
    return "No closing parenthesis"

a0 = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print "Should be 79: is {}".format(matchingParens(a0))
a1 = "((((((("
print "Should have no closing parens: is {}".format(matchingParens(a1))
a2 = ""
print "Should have no closing parens: is {}".format(matchingParens(a2))
a3 = "(())"
print "Should be 3: is {}".format(matchingParens(a3))
