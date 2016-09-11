import unittest


class Singly_LL_Node():

    def __init__(self, val):
        """
        Args:
            val (obj): The value for this node.
            next (Singly_LL_Node): The link to the next node.
        """
        self.val = val
        self.next = None
        self.prev = None


class Singly_LL():

    def __init__(self):
        """
        Args:
            head (Singly_LL_Node): The head of a linked list.
            tail (Singly_LL_Node): The tail of a linked list.
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
            self.head = Singly_LL_Node(val)
            self.tail = self.head
        else:
            new_tail = Singly_LL_Node(val)
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
                self.size -= 1
                if curr == self.head:
                    self.head = curr.next
                    return curr
                elif not curr.next:
                    prev.next = curr.next
                    self.tail = prev
                    return curr
                else:
                    prev.next = curr.next
                    temp = curr
                    curr = curr.next
                    return temp
            else:
                prev = curr
                curr = curr.next

    def print_LL(self):
        """
        Prints a linked list, node by node on the same line.
        """
        curr = self.head
        while curr:
            print curr.val,
            curr = curr.next

    def get_size(self):
        """
        Returns the size of this linked list.
        """
        return self.size


class HashMap():

    def __init__(self, size):
        """ Returns an instance of a HashMap with size number of buckets. """
        self.items = [Singly_LL()] * size
        self.capacity = 0
        self.size = size

    def set(self, key, value):
        if self.capacity >= self.size:
            return False
        """ Returns a boolean value indicating success/failure of the operation. """
        hash_code = hash(key)
        hashed_index = hash_code % self.size
        arr = self.items[hashed_index:] + self.items[:hashed_index]
        for index in xrange(len(arr)):
            if arr[index] == None:
                self.items[index] = [hash_code, value]
                self.capacity += 1
                return True
        return False

    def get(self, key):
        """ Return the value associated with the given key, or null if no value is set. """
        hash_code = hash(key)
        hashed_index = hash_code % self.size
        arr = self.items[hashed_index:] + self.items[:hashed_index]
        for index in xrange(len(arr)):
            if arr[index] != None and arr[index][0] == hash_code:
                return arr[index][1]
        return None

    def delete(self, key):
        """ Delete the value associated with the given key,
        returning the value on success or null if the key has no value. """
        hash_code = hash(key)
        hashed_index = hash_code % self.size
        arr = self.items[hashed_index:] + self.items[:hashed_index]
        for index in arr:
            if arr[index] != None and arr[index][0] == hash_code:
                if arr[index][1] == None:
                    return None
                else:
                    result = arr[index][1]
                    arr[index] = None
                    self.capacity -= 1
                    return result
        return None

    def load(self):
        """ Returns a float value representing the load factor. """
        return float(self.capacity / self.size)


# class TestHashMap(unittest.TestCase):

#     def test_1(self):
#         hashmap = HashMap(5)
#         hashmap.set('a', 1)
#         self.assertEqual(hashmap.get('a'), 1)

if __name__ == "__main__":
    unittest.main()
