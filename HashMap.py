import unittest


class HashMap():

    def __init__(self, size):
        """ Returns an instance of a HashMap with space for num number of items."""
        self.items = [None] * size
        self.num_items = 0
        self.size = size

    def set(self, key, value):
        if self.num_items >= self.size:
            return False
        """ Returns a boolean value indicating success/failure of the operation."""
        hash_code = hash(key)
        hashed_index = hash_code % self.size
        arr = self.items[hashed_index:] + self.items[:hashed_index]
        for index in xrange(len(arr)):
            if arr[index] == None:
                self.items[index] = [hash_code, value]
                self.num_items += 1
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or null if no value is set."""
        hash_code = hash(key)
        hashed_index = hash_code % self.size
        arr = self.items[hashed_index:] + self.items[:hashed_index]
        for index in xrange(len(arr)):
            if arr[index] != None and arr[index][0] == hash_code:
                return arr[index][1]
        return None

    def delete(self, key):
        """Delete the value associated with the given key,
        returning the value on success or null if the key has no value."""
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
                    self.num_items -= 1
                    return result
        return None

    def load(self):
        """Returns a float value representing the load factor."""
        return float(self.num_items / self.size)


class TestHashMap(unittest.TestCase):

    def test_1(self):
        hashmap = HashMap(5)
        hashmap.set('a', 1)
        self.assertEqual(hashmap.get('a'), 1)

if __name__ == "__main__":
    unittest.main()
