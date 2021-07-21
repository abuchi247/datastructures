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
        self.head = self.tail = None
        self.size = 0

    def get_length(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        if data is None:
            print("Data cannot be None")
            return

        new_node = Node(data)
        
        if self.is_empty():    # update the tail and head
            self.head = self.tail = new_node
        else:
            # make new node be the new head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return

    def append(self, data):
        # already implemented logic in prepend method
        if data is None:
            return self.prepend(data)
        
        if self.is_empty():
            return self.prepend(data)

        new_node = Node(data)
        # update the tail node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
        return

    def _traverse_to_index(self, index):
        """
        Optimized traversal
        Big O(N) -> actual goes to N/2
        """
        mid = self.get_length() // 2
        if mid <= index:
            curr = self.head
            counter = 0
            while counter != index:
                curr = curr.next
                counter += 1
            return curr
        else:
            curr = self.tail
            counter = self.get_length() - 1
            while counter != index:
                curr = curr.prev
                counter -= 1
            return curr


    def insert(self, data, index):
        """
        Big O(N)
        """
        if index is None:
            print("Index cannot be None")
            return

        if data is None:
            print("Data cannot be None")
            return

        # edge cases
        if index <= 0:
            return prepend(data)

        if index >= self.get_length():
            return append(data)

        # otherwise, we want to insert data somewhere in the middle
        new_node = Node(data)
        old_node_at_pos = _traverse_to_index(index) # old node at that index
        new_node.prev = old_node_at_pos.prev    # 1, 2, 3, 4 -> 1, 2, 5, 3, 4
        old_node_at_pos.prev = new_node
        new_node.next = old_node_at_pos
        self.size += 1
        return 

    def delete_by_index(self, index):
        """
        Big O(N)
        """
        if index is None:
            print("Index cannot be None")
            return

        if self.is_empty():
            print("List is already empty nothing to delete")
            return

        if index < 0:
            print("Index is less than 0")
            return

        if index >= self.get_length():
            print("Index is greater than number of elements in the list")
            return

        # index is valid
        node_at_pos = self._traverse_to_index(index)
        if node_at_pos == self.head and node_at_pos == self.tail:
            self.head = self.tail = node_at_pos.next
            self.size -= 1
            return
        
        if node_at_pos == self.head:
            self.head = node_at_pos.next
        elif node_at_pos == self.tail:
            self.tail = node_at_pos.prev
        else:
            node_at_pos.prev.next = node_at_pos.next
            node_at_pos.next.prev = node_at_pos.prev
        # unlink the node
        node_at_pos.next = None
        node_at_pos.prev = None
        self.size -= 1

    def delete(self, data):
        """
        Deletes a node in a doubly linked list
        :param data:
        :return:
        """

        if data is None:
            print("Data cannot be None")
            return

        if self.is_empty():
            print("Cannot remove data from an empty list")
            return

        
        curr = self.head

        while curr is not None and curr.data != data:
            curr = curr.next

        # check if data to be removed is not found
        if curr is None:
            print("Oops data not found")
            return

        # check if we had only one element
        if curr == self.head and curr == self.tail:
            self.head = self.tail = curr.next
            self.size -= 1
            return

        # check is data being removed is the head node
        if curr == self.head:
            self.head = curr.next
            self.head.prev = None
        elif curr == self.tail:
            self.tail = curr.prev
            self.tail.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        curr.next = None
        curr.prev = None
        self.size -= 1
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
    # dlist.append(2)
    # dlist.append(4)
    # dlist.append(6)
    dlist.prepend(1)
    print("Head:", dlist.head.data, "tail:", dlist.tail.data)
    print("Before deletion")
    dlist.print_all()
    print("After deleting 0")
    dlist.delete_by_index(0)
    dlist.delete(1)
    print("Head:", dlist.head, "tail:", dlist.tail)
    dlist.print_all()
    print("Noew adding to index 0")
    dlist.prepend(0)
    dlist.append(0)
    dlist.print_all()