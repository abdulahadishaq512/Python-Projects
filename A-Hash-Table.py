class HashTable:
    def __init__(self):
        # User Story 1 & 2: Initialize collection as an empty dictionary
        self.collection = {}

    def hash(self, string):
        # User Story 3, 4, 5, 14: Sum Unicode values using ord()
        return sum(ord(char) for char in string)

    def add(self, key, value):
        # User Story 6, 7, 15, 16, 21, 22: Add with collision handling
        h_index = self.hash(key)
        
        # If the hash index doesn't exist, create a nested dictionary
        if h_index not in self.collection:
            self.collection[h_index] = {}
            
        # Add the specific key-value pair to the nested dictionary
        self.collection[h_index][key] = value

    def remove(self, key):
        # User Story 8, 9, 10, 11, 17: Remove specific key from hash index
        h_index = self.hash(key)
        
        if h_index in self.collection and key in self.collection[h_index]:
            del self.collection[h_index][key]
            
            # Optional cleanup: if the nested dict is now empty, remove the index
            if not self.collection[h_index]:
                del self.collection[h_index]

    def lookup(self, key):
        # User Story 12, 13, 18, 19, 20: Return value or None
        h_index = self.hash(key)
        
        if h_index in self.collection and key in self.collection[h_index]:
            return self.collection[h_index][key]
        
        return None