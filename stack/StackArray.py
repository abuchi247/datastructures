class StackArray:

    MAX_CAPACITY = 2

    def __init__(self):
        self.data = [None] * StackArray.MAX_CAPACITY
        self.size = 0
        self.top = -1


    def is_empty(self):
        """
        checks if the stack is empty

        Big O(1)
        """
        return self.size == 0

    
    def peek(self):
        """
        Gets the top element in the stack

        Big O(1)
        """
        if self.is_empty():
            print("Stack is empty")
            return

        return self.data[self.top]

    
    def pop(self):
        """
        Removes top item in the stack

        Big O(1)
        """
        if self.is_empty():
            print("Stack is empty")
            return
        
        # get the top item
        top_item = self.data[self.top]
        # clear the item in the top position
        self.data[self.top] = None
        # set top to the next position
        self.top = (self.top - 1) % self.MAX_CAPACITY
        # decrement the size
        self.size -= 1
        return top_item

    def push(self, item):
        """
        Pushes an item to the top of the stack

        Big O(1)
        """
        # check if array is full
        if self.size == len(self.data):
            # array is full need to be resized
            self._resize(self.size * 2) # double the array size and copy the contents to the new array

        avail = (self.top + 1) % self.MAX_CAPACITY
        self.data[avail] = item
        self.top = avail
        self.size += 1


    def _resize(self, new_capacity):
        """
        Resize the underlying array by doubling the array capacity

        Big O(N) - N is the size of the current array before doubling
        """
        StackArray.MAX_CAPACITY = new_capacity # set the max capacity to the new capacity
        new_arr = [None] * new_capacity


        for i in range(self.size):
            new_arr[i] = self.data[i]

        self.top = self.size - 1    # set the top back to the nth index
        self.data = new_arr

    def print_all(self):
        """
        Displays all the elements in the stack

        Big O(N)
        """
        print("[", end="")

        walker = self.top

        for i in range(self.size):
            pos = (walker - i) % len(self.data)
            print(self.data[pos], end=" -> ")

        print("None]")


if __name__ == "__main__":
    stack = StackArray()
    stack.push(12)
    stack.push(14)
    stack.push(10)
    stack.push(1)
    stack.push(15)
    stack.push(100)
    print(stack.peek())
    stack.print_all()

    print("Poping top element:", stack.peek())
    stack.pop()
    stack.print_all()
    print("Adding a new top")
    print("Current top:", stack.peek())
    stack.push(50)
    stack.print_all()
    print("Stack MAX CAPACITY: ", stack.MAX_CAPACITY)