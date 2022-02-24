import random


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
        # output = ", ".join([str(val) for val in self.data if val])
        # print(f"[{output}]")
        # for i in range(self.length):
        #     print(self.data[i])
        print(self.data)

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

        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        # remove the last element
        self.data[self.length - 1] = None
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
        return self.sum() / self.length

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

    def insert_sorted(self, value):
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        # check if array is full
        if self.is_full():
            raise Exception("Array is full")

        last_index = self.length - 1
        while last_index >= 0 and self.data[last_index] >= value:
            self.data[last_index + 1] = self.data[last_index]  # copy the current element to the slot next to it
            last_index -= 1
        # insert the element at the last_index + 1
        self.data[last_index + 1] = value
        self.length += 1  # increment the number of elements in the array

    def is_sorted(self):
        """
        Checks if an array is sorted or not
        Time complexity: O(N)
        Space complexity: O(1)
        """
        for i in range(0, self.length - 1):
            if self.data[i] > self.data[i + 1]:
                return False
        return True

    def rearrage(self):
        """
        Rearrage all the -ve number to be on the left side and positive numbers should be on the right side

        Time complexity: O(N)
        Space complexity: O(1)
        """
        start = 0
        end = self.length - 1

        while start < end:
            # increment start until we find a positive number
            if self.data[start] < 0:
                start += 1
                continue
            # decrement end until we get a negative number
            if self.data[end] >= 0:
                end -= 1
            else:
                # swap both numbers
                self.data[start], self.data[end] = self.data[end], self.data[start]
                start += 1
                end -= 1


if __name__ == "__main__":
    arr = Array()
    # arr.add(1)
    # arr.add(2)
    # arr.add(3)
    # arr.add(4)
    # arr.insert(0, 5)
    # arr.insert(5, 2)
    # arr.insert(6, 5)
    # arr.display()
    # arr.delete(0)
    # arr.display()
    # print(arr.min())
    # print(arr.max())
    # print(arr.sum())
    # print(arr.avg())
    # for x in range(5):
    #     value = int(random.random() * 100)
    #     # arr.add()
    #     arr.insert_sorted(value)
    # arr.display()
    # print(arr.is_sorted())

    arr.add(-2)
    arr.add(4)
    arr.add(-3)
    # arr.add(-8)
    # arr.add(7)
    # arr.add(3)

    arr.display()
    arr.rearrage()
    arr.display()
