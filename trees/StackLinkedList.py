class StackOverFlow(Exception):
    pass


class StackUnderFlow(Exception):
    pass


class Node:
    __slots__ = "data", "next"

    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    """
    LIFO data structure

    push(item) - add item to the top of the stack
    pop() - remove the top element from the stack
    is_empty() - check if a stack is empty or not
    peek() - gets the top element in the stack
    get_length() - gets the number of elements in a stack
    """

    MAX_SIZE = 10

    def __init__(self):
        self.top = None
        self.size = 0

    def get_length(self):
        """
        Gets the number of elements in a stack

        Big O(1)
        """
        return self.size

    def is_empty(self):
        """
        Checks if a stack is empty
        Big O(1)
        """
        return self.top is None

    def is_full(self):
        """
        Checks if a stack is full
        Big O(1)
        """
        return self.size == self.MAX_SIZE

    def peek(self):
        """
        Returns the top item in the stack

        Big O(1)
        """
        if self.is_empty():
            raise StackUnderFlow("Stack is empty")

        return self.top.data

    def push(self, item):
        """
        Adds an item to the top a stack

        Big O(1)
        """
        if self.is_full():
            raise StackOverFlow("Stack is already full")

        new_node = Node(item)
        new_node.next = self.top    # make new node to point to the old top item
        self.top = new_node # set the top item to be new node
        self.size += 1    # increment the count of items in stack

    def pop(self):
        """
        Removes the top item from the stack
        Big O(1)
        """
        # check if stack is empty
        if self.is_empty():
            raise StackUnderFlow("Stack is empty")

        top_node = self.top
        self.top = self.top.next    # set the top node to the next node
        self.size -= 1    # decrement the size of the stack
        return top_node.data # node removed

    def print_all(self):
        """
        Displays all the elements in the stack

        Big O(N)
        """
        print("[", end="")

        cur = self.top

        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next

        print("None]")


if __name__ == '__main__':
    stack = StackLinkedList()
    stack.push(12)
    stack.push(14)
    stack.push(10)
    stack.push(10)
    print(stack.peek())
    print(stack.is_full())
    print(stack.is_empty())
    stack.print_all()


