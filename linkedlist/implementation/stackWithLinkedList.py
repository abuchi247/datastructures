class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data


class StackEmptyException(Exception):
    pass


class StackWithLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise StackEmptyException("Stack is empty")
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("Stack is empty")
        data = self.top.data
        next_head = self.top.next
        self.top.next = None
        self.top = next_head
        self.size -= 1
        return data

    def display(self):
        cur = self.top
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


if __name__ == "__main__":
    s = StackWithLinkedList()
    s.display()
    s.push(3)
    s.push(4)
    s.push(5)
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()
    s.push(2)
    s.display()