class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if linked list is empty

        Time complexity: O(1)
        """
        return self.head is None

    def traverse(self):
        """
        Display all the elements in the linked list

        Time complexity: O(N)
        """
        if self.is_empty():
            print("Linkedlist is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=" -> ")
                cur = cur.link
            print("None")

    def add_begin(self, value):
        """
        Add element to the beginning of a linked list
        Time complexity: O(1)
        """
        new_node = Node(value)
        new_node.link = self.head
        self.head = new_node

    def add_end(self, value):
        """
        Add element to the tail of the linked list
        Time complexity: O(N)
        """
        new_node = Node(value)
        # if list is empty
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            # go until we get to the last node
            while cur.link is not None:
                cur = cur.link

            # point the last node next pointer to the new node
            cur.link = new_node

    def add_after(self, target_node, value):
        """
        Add node after the target node
        Time complexity: O(N)
        """
        cur = self.head
        while cur is not None and cur.data != target_node:
            cur = cur.link

        if cur is None:
            print("target node not found")
        else:
            new_node = Node(value)
            new_node.link = cur.link
            cur.link = new_node

    def add_before(self, target_node, value):
        """
        Add node before the target node
        Time complexity: O(N)
        """
        cur = self.head
        while cur is not None and cur.link.data != target_node:
            cur = cur.link

        if cur is None:
            print("target node not found")
        else:
            new_node = Node(value)
            new_node.link = cur.link
            cur.link = new_node

    def delete_head(self):
        """
        Delete the head node of the linked list
        Time complexity: O(1)
        """
        if self.is_empty():
            print("linked list is empty")
        else:
            self.head = self.head.link

    def delete_last(self):
        """
        Delete the tail node from the linked list
        Time complexity: O(N)
        """
        if self.is_empty():
            print("Linked list is empty")
        else:
            cur = self.head
            prev = None
            while cur.link is not None:
                prev = cur
                cur = cur.link
            # update the link of the second to the last node to point to None
            if prev is not None:
                prev.link = None
            else:
                self.head = None

    def delete_by_value(self, value):
        """
        Delete a node based on it's value. using the first occurrence of the value
        Time complexity: O(N)
        """
        if self.is_empty():
            print("Linked list is empty")

        prev = None
        cur = self.head
        while cur is not None and cur.data != value:
            prev = cur
            cur = cur.link

        if cur is None:
            print("Value not found")
        else:
            # found at the head
            if prev is None:
                self.head = cur.link
            else:
                prev.link = cur.link
                cur.link = None


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.add_end(2)
    ll.add_end(3)
    ll.add_end(4)
    ll.add_begin(5)
    ll.add_begin(0)
    ll.traverse()
    ll.add_after(target_node=2, value=10)
    ll.traverse()
    ll.add_before(target_node=2, value=10)
    ll.traverse()
    print("deleting from a linked list")
    ll.delete_head()
    ll.traverse()
    ll.delete_last()
    ll.traverse()
    print("delete node by value")
    ll.delete_by_value(10)
    ll.traverse()

