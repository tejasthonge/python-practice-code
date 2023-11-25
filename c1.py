class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.buckets[index] is None:
            self.buckets[index] = [(key, value)]
        else:
            for pair in self.buckets[index]:
                if pair[0] == key:
                    pair = (key, value)
                    return
            self.buckets[index].append((key, value))

    def retrieve(self, key):
        index = self.hash_function(key)
        if self.buckets[index] is not None:
            for pair in self.buckets[index]:
                if pair[0] == key:
                    return pair[1]
        return None

# Example usage:
hash_table = HashTable()
hash_table.insert('name', 'John')
hash_table.insert('age', 30)
hash_table.insert('city', 'New York')

print(hash_table.retrieve('name'))  # Output: John
print(hash_table.retrieve('age'))   # Output: 30
print(hash_table.retrieve('city'))  # Output: New York
print(hash_table.retrieve)

