import unittest


class Singly_LL_Node():

    def __init__(self, key, val):
        """
        Args:
            val (obj): The value for this node.
            next (Singly_LL_Node): The link to the next node.
        """
        self.key = key
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

    def add(self, key, val):
        """
        Args:
            val (obj): The value for a new node to be added to this linked list.
        """
        if self.head == None:
            self.head = Singly_LL_Node(key, val)
            self.tail = self.head
        else:
            new_tail = Singly_LL_Node(key, val)
            self.tail.next = new_tail
            self.tail = new_tail
        self.size += 1

    def remove(self, key):
        """
        Args:
            val (obj): The value for the node to be removed.
        """
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                self.size -= 1
                if curr == self.head:
                    self.head = curr.next
                    return curr.val
                elif not curr.next:
                    prev.next = curr.next
                    self.tail = prev
                    return curr.val
                else:
                    prev.next = curr.next
                    temp = curr
                    curr = curr.next
                    return temp.val
            else:
                prev = curr
                curr = curr.next
        return None

    def get(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.val
            else:
                curr = curr.next
        return None

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
        self.num_buckets = size
        self.array = [Singly_LL()] * self.num_buckets
        self.capacity = 0
        self.load_factor = .70
        self.threshold = (self.load_factor * self.num_buckets)

    def set(self, key, value):
        if self.capacity >= self.threshold:
            # redistribute all existing entries
            return False
        """ Returns a boolean value indicating success/failure of the operation. """
        hash_code = hash(key)
        hashed_index = hash_code & self.num_buckets - 1
        ll = self.array[hashed_index]
        ll.add(key, value)
        self.capacity += 1
        return True

    def get(self, key):
        """ Return the value associated with the given key, or null if no value is set. """
        hash_code = hash(key)
        hashed_index = hash_code & self.num_buckets - 1
        ll = self.array[hashed_index]
        return ll.get(key)

    def delete(self, key):
        """ Delete the value associated with the given key,
        returning the value on success or null if the key has no value. """
        hash_code = hash(key)
        hashed_index = hash_code & self.num_buckets - 1
        ll = self.array[hashed_index]
        return ll.remove(key)

    def load(self):
        """ Returns a float value representing the load factor. """
        return float(self.capacity / self.threshold)


# class TestHashMap(unittest.TestCase):

#     def test_1(self):
#         hashmap = HashMap(5)
#         hashmap.set('a', 1)
#         self.assertEqual(hashmap.get('a'), 1)

if __name__ == "__main__":
    unittest.main()
