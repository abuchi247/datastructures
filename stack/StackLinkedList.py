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

    def __init__(self):
        self.top = None
        self.length = 0

    def get_length(self):
        """
        Gets the number of elements in a stack

        Big O(1)
        """
        return self.length

    def is_empty(self):
        """
        Checks if a stack is empty
        Big O(1)
        """
        return self.top is None

    def peek(self):
        """
        Returns the top item in the stack

        Big O(1)
        """
        if self.is_empty():
            print("Stack is empty")
            return
        return self.top

    def push(self, item):
        """
        Adds an item to the top a stack

        Big O(1)
        """
        new_node = Node(item)

        new_node.next = self.top    # make new node to point to the old top item
        self.top = new_node # set the top item to be new node
        self.length += 1    # increment the count of items in stack

    def pop(self):
        """
        Removes the top item from the stack
        Big O(1)
        """
        # check if stack is empty
        if self.is_empty():
            print("Stack is empty")
            return

        top_node = self.top

        self.top = self.top.next    # set the top node to the next node
        self.length -= 1    # decrement the size of the stack
        return top_node # node removed

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
    print(stack.peek().data)
    stack.print_all()


