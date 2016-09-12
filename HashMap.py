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
            key (str): The key for the node to be removed. 

        Returns:
            val (obj): The key's value if the key we wanted was found. Value if success,
            None otherwise.
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
        """
        Args:
            key (str): The key for the node to be queried.

        Returns:
            val (obj): The key's value if the key we wanted was found. Value if success,
            None otherwise.            
        """
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
        Use for debugging. 
        """
        curr = self.head
        while curr:
            print curr.val,
            curr = curr.next

    def get_size(self):
        """
        Returns:
            size (int): The size of this linked list.
        """
        return self.size


class HashMap():

    def __init__(self, size):
        """ 
        Args:
            size (int): The number of buckets for the HashMap's internal array.

        Raises:
            ValueError: If size <= 1.
        """
        if size <= 0:
            raise ValueError(
                "A HashMap can only be instantiated with size >= 1.")

        self.num_buckets = size
        self.array = [None] * self.num_buckets
        self.capacity = 0
        self.threshold = .70

    def set(self, key, value):
        """ 
        Args:
            key (str): The key we want to set.
            value (obj): The value we want to set for the associated key.

        Returns:
            bool: True if successful operation, False otherwise.
        """
        self.capacity += 1
        if self.load() >= self.threshold:
            # resize and redistribute all existing entries
            self.new_num_buckets = self.num_buckets * 2
            self.new_array = [None] * (self.new_num_buckets)
            for ll in self.array:
                if ll:
                    curr = ll.head
                    while curr:
                        old_key, old_val = curr.key, curr.val
                        new_hash_code = hash(old_key)
                        new_hashed_index = new_hash_code & (
                            self.new_num_buckets - 1)
                        if self.new_array[new_hashed_index]:
                            ll = self.new_array[new_hashed_index]
                            ll.add(old_key, old_val)
                        else:
                            ll = Singly_LL()
                            self.new_array[new_hashed_index] = ll
                            ll.add(old_key, old_val)
                        curr = curr.next
            self.array = self.new_array
            self.num_buckets = self.new_num_buckets
        hash_code = hash(key)
        hashed_index = hash_code & (self.num_buckets - 1)
        if self.array[hashed_index]:
            ll = self.array[hashed_index]
            ll.add(key, value)
        else:
            ll = Singly_LL()
            self.array[hashed_index] = ll
            ll.add(key, value)
        return True

    def get(self, key):
        """ 
        Args:
            key (str): The key we use to find the value we want. 

        Returns:
            val (obj): The value if it is found. Returns None otherwise.
        """
        hash_code = hash(key)
        hashed_index = hash_code & self.num_buckets - 1
        if self.array[hashed_index]:
            ll = self.array[hashed_index]
            return ll.get(key)
        else:
            return None

    def delete(self, key):
        """ 
        Args: 
            key (str): The key we use to delete the value we want.

        Returns:
            val (obj): The value if we found and deleted it successfully. 
            None if otherwise.
        """
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
        """ 
        Returns:
            load (float): a float value representing the load factor. 
        """
        return float(self.capacity) / self.num_buckets


class TestHashMap(unittest.TestCase):

    def test_trivial_get(self):
        example = HashMap(1)
        example.set('hi', 'yo')
        self.assertEqual(example.get('hi'), 'yo')

    def test_trivial_delete(self):
        example = HashMap(1)
        example.set('hi', 'yo')
        self.assertEqual(example.delete('hi'), 'yo')
        self.assertEqual(example.load(), 0)

    def test_trivial_all(self):
        example = HashMap(3)
        example.get('3')
        self.assertEqual(example.get(3), None)
        example.set('3', "hello!")
        self.assertEqual(example.get('3'), "hello!")
        example.set('1', 2)
        self.assertEqual(example.load(), 2 / 3.0)
        example.set('6', 7)
        self.assertEqual(example.get('6'), 7)
        example.load()
        self.assertEqual(example.load(), 3 / 6.0)
        example.set('8', 9)
        example.load()
        self.assertEqual(example.get('8'), 9)
        example.set('10', 11)
        example.load()
        self.assertEqual(example.load(), 5 / 12.0)
        example.delete('6')
        self.assertEqual(example.get('6'), None)
        self.assertEqual(example.load(), 4 / 12.0)
        self.assertEqual(example.delete('10'), 11)
        self.assertEqual(example.delete('10'), None)

    def test_get(self):
        example = HashMap(2**20)
        example.set('hi', 'yo')
        self.assertEqual(example.load(), 1.0 / 2**20)

if __name__ == "__main__":
    unittest.main()
