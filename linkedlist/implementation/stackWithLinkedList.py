import copy

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

    def delete_all(self):
        while self.top is not None:
            print(f"Freeing: {self.top.data}")
            next = self.top.next
            self.top.next = None
            del self.top
            self.top = next

    def insert_nth(self, data, nth):
        new_node = Node(data)
        index = 0
        prev = None
        cur = self.top

        while cur is not None and index < nth:
            prev = cur
            cur = cur.next
            index += 1
        # insert at the beginning
        if prev is None:
            self.top = new_node
        else:
            prev.next = new_node
        new_node.next = cur
        self.size += 1

    def insert_sorted(self, data):
        new_node = Node(data)
        prev = None
        cur = self.top

        while cur is not None and cur.data < data:
            prev = cur
            cur = cur.next

        if prev is None:
            self.top = new_node
        else:
            prev.next = new_node
        new_node.next = cur


if __name__ == "__main__":
    s = StackWithLinkedList()
    # s.display()
    # s.push(3)
    # s.push(4)
    # s.push(5)
    # s.display()
    # s.pop()
    # s.display()
    # s.pop()
    # s.display()
    # s.push(2)
    # s.display()
    #
    # for x in range(10):
    #     s.push(x**2)
    #
    # s.display()
    # s.delete_all()
    # print(s.top)
    # s.display()
    #
    # s.insert_nth(1, 5)
    # s.display()
    # s.insert_nth(2, 11)
    # s.display()
    # s.insert_nth(2, -11)
    # s.display()
    # s.insert_nth(20, 1)
    # s.display()
    # s.insert_nth(50, 3)
    # s.display()

    s.insert_sorted(4)
    s.display()
    s.insert_sorted(10)
    s.display()
    s.insert_sorted(2)
    s.display()
    s.insert_sorted(5)
    s.display()
    s.insert_sorted(20)
    s.display()