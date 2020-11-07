# MAXIMUM_SIZE = 10
# get_length() -> return the number of elements in array
# get(index) -> return the item at index location or out of bound exception if the index is greater than number of items or less than 0
# delete(index) -> remove an item at index location or out of bound exception if the index is greater than number of items or less than 0
# insert(data) -> add an item to the end of the array and resize if it's already full
# _resize -> resize the array if it's getting full

class OutOfBoundException(Exception):
    pass

class TypeException(Exception):
    pass

class DynamicArray:
    MAXIMUM_SIZE = 3

    def __init__(self):
        self.data = [None] * self.MAXIMUM_SIZE # populate the data with Nones
        self.size = 0

    
    def get_length(self):
        """
        Return the number of items in the array

        Big O(1)
        """
        return self.size

    
    def get(self, index):
        """
        Return the data of the item at index location
        """
        if index is None:
            raise TypeException("Invalid index value specified")

        if not isinstance(index, int):
            raise TypeException("Invalid index value specified")

        # check if the index is valid
        if index < 0 or index >= self.get_length():
            raise OutOfBoundException("Index valud is out of bound")

        return self.data[index] # return item at index location

    
    def insert(self, value):
        """
        Inserts value to the end of the array
        """
        if self.get_length() == len(self.data):
            self._resize()

        self.data[self.get_length()] = value
        self.size += 1

    
    def delete(self, index):
        """
        Delete item at index location
        """
        if index is None:
            raise TypeException("Invalid index value specified")

        if not isinstance(index, int):
            raise TypeException("Invalid index value specified")

        # check if the index is valid
        if index < 0 or index >= self.get_length():
            raise OutOfBoundException("Index valud is out of bound")

        i = index

        while i < self.get_length():
            self.data[i] = self.data[i+1]
            i += 1
        
        self.data[i] = None# clear the content of the last element

        self.size -= 1



    def print_array(self):
        print("[", end="")
        for i in range(self.get_length()):
            if i + 1 != self.get_length():
                print(self.data[i], end=", ")
            else:
                print(self.data[i], end="")
        print("]")


    def _resize(self):
        """
        Doubles the size of the array
        """
        current_size = len(self.data)
        new_size = current_size * 2

        new_data = [None] * new_size

        for i in range(current_size):
            new_data[i] = self.data[i]
        
        self.data = new_data
    
if __name__ == "__main__":
    array = DynamicArray()
    print(array.get_length())
    array.insert(2)
    array.insert(3)
    array.insert(1)
    array.insert(4)
    array.print_array()
    # print(array.get_length())
    # print(array.get(3))

    array.delete(2)
    array.print_array()