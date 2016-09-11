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
        if size <= 0:
            raise ValueError(
                "A HashMap can only be instantiated with size >= 1.")

        self.num_buckets = size
        self.array = [None] * self.num_buckets
        self.capacity = 0
        self.threshold = (.70 * self.num_buckets)

    def set(self, key, value):
        if self.load() >= self.threshold:
            # resize and redistribute all existing entries
            return False
        """ Returns a boolean value indicating success/failure of the operation. """
        hash_code = hash(key)
        hashed_index = hash_code & self.num_buckets - 1
        if self.array[hashed_index]:
            ll = self.array[hashed_index]
            ll.add(key, value)
        else:
            ll = Singly_LL()
            self.array[hashed_index] = ll
            ll.add(key, value)
        self.capacity += 1
        return True

    def get(self, key):
        """ Return the value associated with the given key, or null if no value is set. """
        hash_code = hash(key)
        hashed_index = hash_code & self.num_buckets - 1
        if self.array[hashed_index]:
            ll = self.array[hashed_index]
            return ll.get(key)
        else:
            return None

    def delete(self, key):
        """ Delete the value associated with the given key,
        returning the value on success or null if the key has no value. """
        hash_code = hash(key)
        hashed_index = hash_code & self.num_buckets - 1
        if self.array[hashed_index]:
            ll = self.array[hashed_index]
            result = ll.remove(key)
            if result:
                self.capacity -= 1
                return result
        return None

    def load(self):
        """ Returns a float value representing the load factor. """
        return float(self.capacity) / self.num_buckets


# class TestHashMap(unittest.TestCase):

#     def test_1(self):
#         print a.set(3, 5)
# a = HashMap(5)
# print a.get(3)
# print a.delete(3)
# print a.get(3)
# print a.set(1, 2)
# print a.set(6, 7)
# print a.set(8, 9)
# print a.set(10, 11)
# print a.set(12, 13)
# print a.delete(6)
# print a.delete(10)
# print a.delete(50)
# print a.load()

#         self.assertEqual(hashmap.get('a'), 1)

# if __name__ == "__main__":
#     unittest.main()
