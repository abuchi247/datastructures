class ArrayOverflowException(Exception):
    pass


class ArrayUnderflowException(Exception):
    pass


class Array:

    def __init__(self, size=10):
        self.size = size
        self.length = 0
        self.data = [None] * size

    def display(self):
        """
        Displays all the elements in the array
        Time complexity: O(N)
        Space complexity: O(1)
        """
        output = ", ".join([str(val) for val in self.data if val])
        print(f"[{output}]")
        # for i in range(self.length):
        #     print(self.data[i])

    def add(self, value):
        """
        Adds an element to the tail of the array

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.length >= self.size:
            raise ArrayOverflowException("Array full")

        self.data[self.length] = value
        self.length += 1

    def insert(self, index, value):
        """
        Inserts a value at a given index
        Time complexity: O(N)
        Space complexity: O(1)
        """
        if index < 0:
            raise ArrayUnderflowException("Index out of bound")
        elif index > self.length:
            raise ArrayOverflowException("Index out of bound")

        if self.length >= self.size:
            raise ArrayOverflowException("Array full")

        # move elements around to make room
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.length += 1

    def delete(self, index):
        """
        Deletes an element from a given index
        Time complexity: O(N)
        Space complexity: O(1)
        """
        if index < 0:
            raise ArrayUnderflowException("Invalid Index")

        elif index >= self.length:
            raise ArrayOverflowException("Invalid index")

        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

        # remove the last element
        self.data[self.length-1] = None
        self.length -= 1


if __name__ == "__main__":
    arr = Array()
    arr.add(1)
    arr.add(1)
    arr.add(1)
    arr.add(1)
    arr.insert(0, 5)
    arr.insert(5, 2)
    arr.insert(6, 5)
    arr.display()
    arr.delete(0)
    arr.display()