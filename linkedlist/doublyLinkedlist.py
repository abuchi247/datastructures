class Node:
    """
    Implements the nodes in a doubly linked list
    """
    __slots__ = "data", "prev", "next"

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def get_length(self):
        curr = self.head
        size = 0

        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def delete(self, data):
        """
        Deletes a node in a doubly linked list
        :param data:
        :return:
        """
        curr = self.head

        while curr is not None and curr.data != data:
            curr = curr.next

        # data not found
        if curr is None:
            return

        # check if the data is to be removed is the head node
        if curr.prev is None:
            self.head = curr.next
        else:   # otherwise, we set the prev next point to the curr node next node
            curr.prev.next = curr.next

        if curr.next is not None:   # ensure the data to be removed is not the last node
            curr.next.prev = curr.prev  # point the next pointer prev node to the cur prev node

        # unlink the curr from the doubly linked list
        curr.prev = None
        curr.next = None
        curr = None
        return

    def append(self, data):
        """
        Add a new node to the doubly linked list
        :param data:
        :return:
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # we have at least one element in the doubly linked list
        curr = self.head

        # iterate until we get to the last node
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr
        return

    def print_all(self):
        """
        This method prints all the elements in a linked list
        :return:
        """
        curr = self.head

        print("[", end="")
        while curr is not None:
            print(f"{curr.data} -> ", end="")
            curr = curr.next
        print("None]")


if __name__ == "__main__":
    dlist = DoublyLinkedList()
    dlist.append(2)
    dlist.append(4)
    dlist.append(6)
    print("Before deletion")
    dlist.print_all()
    print("After deleting 2")
    dlist.delete(6)
    dlist.print_all()