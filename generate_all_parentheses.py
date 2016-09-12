"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
import Stack as S


def match(char1, char2):
    if char1 == '(' and char2 == ')':
        return True
    elif char1 == '{' and char2 == '}':
        return True
    elif char1 == '[' and char2 == ']':
        return True
    else:
        return False


def is_valid(s):
    stack = S.Stack()
    for i, char in enumerate(s):
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        elif char == ')' or char == '}' or char == ']':
            if stack.is_empty() or not match(stack.peek(), char):
                return 0
            else:
                stack.pop()
        else:
            return 0

    return 1 if stack.size() == 0 else 0

print is_valid("({[])")
