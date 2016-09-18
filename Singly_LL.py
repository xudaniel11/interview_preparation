"""
Singly linked list implementation

@author: Jasmine Lee
"""


class Single_LLNode():

    def __init__(self, val):
        """
        Args: 
            val (obj): The value for this node.
            next (Single_LLNode): The link to the next node.
        """
        self.val = val
        self.next = None


class Singly_LL():

    def __init__(self):
        """
        Args: 
            head (Single_LLNode): The head of a linked list.
            tail (Single_LLNode): The tail of a linked list.
            size (int): The number of nodes in this linked list.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        """
        Args: 
            val (obj): The value for a new node to be added to this linked list.
        """
        if self.head == None:
            self.head = Single_LLNode(val)
            self.tail = self.head
        else:
            new_tail = Single_LLNode(val)
            self.tail.next = new_tail
            self.tail = new_tail
        self.size += 1

    def remove(self, val):
        """
        Args: 
            val (obj): The value for the node(s) to be removed. Every node with this val
            will be removed from the linked list.
        """
        curr = self.head
        prev = None
        while curr:
            if curr.val == val:
                if curr == self.head:
                    # prev.next = curr.next
                    self.head = curr.next
                    curr = curr.next
                elif not curr.next:
                    prev.next = curr.next
                    self.tail = prev
                    curr = curr.next
                else:
                    prev.next = curr.next
                    # prev = curr
                    curr = curr.next
                self.size -= 1
            else:
                prev = curr
                curr = curr.next

    def print_LL(self):
        """
        Prints a linked list, node by node on the same line.
        """
        curr = self.head
        result = []
        while curr:
            print curr.val,
            curr = curr.next

    def get_size(self):
        """
        Returns the size of this linked list.
        """
        return self.size


def test():
    exampleLL = Singly_LL()
    exampleLL.add(1)
    exampleLL.add(1)
    exampleLL.add(2)
    exampleLL.add(3)
    exampleLL.add(1)
    exampleLL.add(1)
    exampleLL.add(4)
    exampleLL.add(1)
    exampleLL.add(1)
    exampleLL.print_LL()
    print "\n"

    exampleLL.remove(1)
    exampleLL.print_LL()
