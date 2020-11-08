class HashTable:

    def __init__(self, size):
        self.slots = [None]*size
        self.data = [None]*size
        self.size = size

    def hash(self, key):
        return key % self.size

    def rehash(self, oldHashkey):
        return (oldHashkey + 1) % self.size

    def put(self, key, value):
        '''Linear probing solution'''
        '''Downside is if all the spaces are taken, it will go into an infinite loop'''

        hash_value = self.hash(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_key = self.rehash(hash_value)
                while self.slots[next_key] is not None and self.slots[next_key] != key:
                    next_key = self.rehash(next_key)
                if self.slots[next_key] == None:
                    self.slots[next_key] = key
                    self.data[next_key] = value
                else:
                    self.data[next_key] = value

    def putNode(self, key, value):
        '''Collision solution using chaining technique'''
        hashvalue = self.hash(key)
        tempKeys = []
        tempValues = []
        if self.slots[hashvalue] == None:
            tempKeys.append(key)
            tempValues.append(value)
            self.slots[hashvalue] = tempKeys
            self.data[hashvalue] = tempValues
        else:
            if key in self.slots[hashvalue]:
                location = self.slots[hashvalue].index(key)
                self.data[hashvalue][location] = value
            else:
                self.slots[hashvalue].append(key)
                self.data[hashvalue].append(value)

    def getNode(self, key):
        hashvalue = self.hash(key)
        if self.slots[hashvalue] == None:
            return "No data"
        else:
            for index, value in enumerate(self.slots[hashvalue]):
                if value == key:
                    return self.data[hashvalue][index]
            return "No data"

    def get(self, key):
        hash_value  = self.hash(key)

        if self.slots[hash_value] is None:
            return "No data"
        else:
            if self.slots[hash_value] == key:
                return self.data[hash_value]
            else:
                next_key = self.rehash(hash_value)
                while self.slots[next_key] is not None and self.slots[next_key] != key:
                    next_key = self.rehash(next_key)
                if self.slots[next_key] == None:
                    return "No data"
                else:
                    return self.data[next_key]


if __name__ == "__main__":
    myhash = HashTable(2)
    myhash.putNode(1, 1000)
    myhash.putNode(2, 2000)
    myhash.putNode(3, 3000)
    myhash.putNode(3, 4000)
    # myhash.put(100, 4000)
    
    print(myhash.slots)
    print(myhash.data)
    print(myhash.getNode(1))