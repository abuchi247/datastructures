class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def is_empty(self):
        """
        Checks if a linked list is empty

        Time complexity: O(1)
        """
        return self.head is None

    def traverse_forward(self):
        """
        Prints elements in the linked list from head to tail
        Time complexity: O(N)
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=" <----> ")
                cur = cur.next
            print("None")

    def traverse_backward(self):
        """
        Prints elements in the linked list from tail to head
        Time complexity: O(N)
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            cur = self.tail
            while cur is not None:
                print(cur.data, end=" <----> ")
                cur = cur.prev
            print("None")

    def add_head(self, value):
        """
        Add a node to the head of a linked list
        Time complexity: O(1)
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_tail(self, value):
        """
        Add a node to the tail of a linked list
        Time complexity: O(1)
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_after(self, target_node, value):
        """
        Add node after the target node
        Time complexity: O(N)
        """
        cur = self.head
        while cur is not None and cur.data != target_node:
            cur = cur.next

        if cur is None:
            print("target node not found")
        else:
            # add to the head
            if cur == self.head:
                self.add_head(value)
            # add to the tail
            elif cur == self.tail:
                self.add_tail(value)
            # add in-between
            else:
                new_node = Node(value)
                new_node.prev = cur
                new_node.next = cur.next
                cur.next.prev = new_node
                cur.next = new_node

    def delete_head(self):
        """
        Deletes the head node from a linked list
        Time complexity: O(1)
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def delete_tail(self):
        """
        Deletes the tail node from the linked list
        Time complexity: O(1)
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def delete_by_value(self, value):
        """
        Delete the first occurrence of a value from the linked list
        Time complexity: O(N)
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            cur = self.head
            while cur is not None and cur.data != value:
                cur = cur.next

            if cur is None:
                print(f"{value} not found")
            else:
                if cur == self.head:    # delete head node
                    self.delete_head()
                elif cur == self.tail:  # delete tail node
                    self.delete_tail()
                else:   # delete in between node
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur.next = None
                    cur.prev = None


if __name__ == "__main__":
    dd = DoublyLinkedList()
    dd.add_tail(1)
    dd.add_tail(2)
    dd.add_tail(3)
    dd.add_tail(4)
    dd.add_tail(5)
    dd.traverse_forward()
    # dd.traverse_backward()
    dd.add_after(5, 0)
    dd.add_after(2, 0)
    dd.traverse_forward()
    # dd.traverse_backward()
    print("deleting nodes")
    dd.delete_by_value(0)
    dd.delete_by_value(0)
    dd.traverse_forward()
    dd.traverse_backward()