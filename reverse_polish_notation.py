"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

import Stack as S
import unittest


def reverse_polish_notation(arr):
    stack = S.Stack()
    for i, char in enumerate(arr):
        if char.isdigit() or (char.startswith('-') and char[1:].isdigit()):
            stack.push(char)
        else:
            op2 = str(stack.pop())
            op1 = str(stack.pop())
            result = eval(op1 + char + op2)
            stack.push(str(result))
    return stack.peek() if stack.size() == 1 else False

# print reverse_polish_notation(["2", "1", "+", "3", "*"])
# print reverse_polish_notation(["4", "13", "5", "/", "+"])
# print reverse_polish_notation(['5', '1', '2', '+', '4', '*', '+', '3', '-'])
print reverse_polish_notation(["-500", "-10", "/"])
