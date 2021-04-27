class OutBoundException(Exception):
    pass


class Array:

    def __init__(self, size=10):
        self.size = size
        self.length = 0
        self.data = [None] * size

    def is_full(self):
        return self.length == self.size

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
        if self.is_full():
            raise OutBoundException("Array full")

        self.data[self.length] = value
        self.length += 1

    def insert(self, index, value):
        """
        Inserts a value at a given index
        Time complexity: O(N)
        Space complexity: O(1)
        """
        if index < 0 or index > self.length:
            raise OutBoundException("Index out of bound")

        if self.is_full():
            raise OutBoundException("Array full")

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
        if index < 0 or index >= self.length:
            raise OutBoundException("Index is out of bound")

        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

        # remove the last element
        self.data[self.length-1] = None
        self.length -= 1

    def get(self, index):
        """
        Get the element at a particular index

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if index < 0 or index >= self.length:
            raise OutBoundException("Invalid index")

        return self.data[index]

    def set(self, index, value):
        """
        Replace a value at a particular index

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if index < 0 or index >= self.length:
            raise OutBoundException("Invalid index")

        self.data[index] = value

    def max(self):
        """
        Get the maximum element in the array

        Time complexity: O(N)
        Space complexity: O(1)
        """
        if self.length == 0:
            raise Exception("Array is empty")

        max_value = self.data[0]

        for i in range(1, self.length):
            if self.data[i] > max_value:
                max_value = self.data[i]

        return max_value

    def min(self):
        """
        Get the minimum element in the array

        Time complexity: O(N)
        Space complexity: O(1)
        """
        if self.length == 0:
            raise Exception("Array is empty")

        min_value = self.data[0]

        for i in range(1, self.length):
            if self.data[i] < min_value:
                min_value = self.data[i]

        return min_value

    def avg(self):
        """
        Find the average of all the elements in the array

        Time complexity: O(N)
        Space complexity: O(1)
        """
        return self.sum()/self.length

    def sum(self):
        """
        Find the sum of all elements in the array

        Time complexity: O(N)
        Space complexity: O(1)
        """
        if self.length == 0:
            raise Exception("Array is empty")

        total = 0

        for i in range(self.length):
            total += self.data[i]

        return total


def shift_left_rotate(arr, shifts):
    if len(arr) <= 1:
        return

    for _ in range(shifts):
        shift_left(arr)


def shift_left(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr) - 1] = temp


if __name__ == "__main__":
    arr = Array()
    arr.add(1)
    arr.add(2)
    arr.add(3)
    arr.add(4)
    arr.insert(0, 5)
    arr.insert(5, 2)
    arr.insert(6, 5)
    arr.display()
    arr.delete(0)
    arr.display()
    print(arr.min())
    print(arr.max())
    print(arr.sum())
    print(arr.avg())

    arr.display()
    shift_left_rotate(arr.data, 2)
    arr.display()