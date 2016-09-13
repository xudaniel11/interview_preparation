"""
Queue DS
"""


class Queue():

    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    def front(eslf):
        return A[0]
