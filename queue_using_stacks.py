"""
Implement a queue using two stacks.
"""
import Stack as S
import unittest


class MyQueue():

    def __init__(self):
        self.s1 = S.Stack()
        self.s2 = S.Stack()
        self.size = 0

    def enqueue(self, val):
        self.s1.push(val)
        self.size += 1

    def dequeue(self):
        s2 = self.s2
        s1 = self.s1
        if not s2.is_empty():
            return s2.pop()
        else:
            while not s1.is_empty():
                s2.push(s1.pop())
            self.size -= 1
            return s2.pop()

    def peek(self):
        s2 = self.s2
        s1 = self.s1
        if not s2.is_empty():
            return s2.peek()
        else:
            while not s1.is_empty():
                s2.push(s1.pop())
            return s2.peek()


class TestMyQueue(unittest.TestCase):

    def test_1(self):
        a = [1, 6, 4, 10, 2, 5]
        q = MyQueue()
        for each in a:
            q.enqueue(each)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.peek(), 6)
        q.enqueue(999)
        self.assertEqual(q.dequeue(), 6)
        self.assertEqual(q.peek(), 4)
if __name__ == "__main__":
    unittest.main()
