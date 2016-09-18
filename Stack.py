"""
A Stack DS using a list.
"""


class Stack():

    def __init__(self):
        self.ls = []

    def push(self, elem):
        self.ls.append(elem)

    def pop(self):
        return self.ls.pop()

    def is_empty(self):
        return len(self.ls) == 0

    def peek(self):
        return self.ls[-1] if len(self.ls) > 0 else None

    def size(self):
        return len(self.ls)

a = Stack()
for i in range(5):
    a.push(i)

# print a.pop()  # should be 4
# print a.peek()  # 3
# print a.size()  # 4
