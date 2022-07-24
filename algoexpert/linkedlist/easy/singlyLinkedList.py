class LinkedListUnderFlowException(Exception):
    pass


class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, new_next):
        self.__next = new_next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def show(self):
        """
        Prints all the elements in the linkedlist

        Time complexity: O(N)
        Space complexity: O(1)
        """
        cur = self.head
        while cur is not None:
            print(cur.get_data(), end=" -> ")
            cur = cur.get_next()
        print("None")

    def is_empty(self):
        """
        Checks if the linked list is empty or not

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.head is None

    def append(self, data):
        """
        Appends data to the end of a linked list

        Time complexity: O(N)
        Space complexity: O(1)
        """
        new_node = Node(data)

        # check if the linked list empty
        if self.is_empty():
            self.head = new_node
            return

        cur = self.head
        # iterate until you get to the end of the linked list
        while cur.get_next() is not None:
            cur = cur.get_next()

        # link the last empty to the new node
        cur.set_next(new_node)
        return

    def pop_first(self):
        """
        Removes the first element from the linkedlist

        Time complexity: O(1)
        Space complexty: O(1)
        """
        if self.is_empty():
            raise LinkedListUnderFlowException("Linked list is empty")

        # store the node we want to remove
        popped_element = self.head
        print(f"Freeing: {popped_element.get_data()}")
        # set the head node to point to the next node from the head
        self.head = self.head.get_next()
        return popped_element.get_data()

    def delete_all(self):
        """
        Delete everything in the linkedlist

        Time complexity: O(N)
        Space complexity: O(1)
        """
        while self.head is not None:
            print(f"Freeing: {self.head.get_data()}")
            # store the next node in a temp variable
            next = self.head.get_next()
            # override the link to the next node with None
            self.head.set_next(None)
            # set head to the next node
            self.head = next

    def insert_nth(self, data, nth):
        """
        Inserts a node at the nth position

        Time complexity: O(N)
        Space complexity: O(1)
        """
        if nth < 0:
            raise LinkedListUnderFlowException(f"nth should be >= 0 expect, got {nth}")

        cur = self.head
        prev = None
        index = 0
        new_node = Node(data)
        # iterate until we get to nth position or we get to the last element in the linked list
        while cur is not None and index < nth:
            index += 1
            prev = cur
            cur = cur.get_next()

        # we want to add new node to the beginning of the linked list
        if prev is None:
            self.head = new_node
        else:
            # found the nth position and adding new node to it
            prev.set_next(new_node)
        # link new node to the next element
        new_node.set_next(cur)
        return

    def insert_sorted(self, data):
        """
        Insert items to the linked list in a sorted matter

        Time complexity: O(N)
        Space complexity: O(1)
        """
        prev = None
        cur = self.head

        while cur is not None and cur.get_data() < data:
            prev = cur
            cur = cur.get_next()

        new_node = Node(data)
        # insert at the beginning and setting head node to point to the newly inserted node
        if prev is None:
            self.head = new_node
        else: # we are somewhere in the middle and need to set the prev node to point to the new node
            prev.set_next(new_node)
        # set new node to point to the current node
        new_node.set_next(cur)


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    linkedList.insert_sorted(2)
    linkedList.insert_sorted(2)
    linkedList.insert_sorted(200)
    linkedList.show() # 2 -> None
    linkedList.insert_sorted(-1)
    linkedList.insert_sorted(0)
    linkedList.insert_sorted(10)
    linkedList.show() # -1 -> 0 -> 2 -> 10 -> None



    # linkedList.append(12)
    # linkedList.append(0)
    # linkedList.append(2)
    # linkedList.show()
    # linkedList.pop_first()
    # linkedList.append(1)
    # linkedList.show()
    # linkedList.insert_nth(50, 0)
    # linkedList.insert_nth(10, 5)
    # linkedList.show()
    # linkedList.delete_all()
    # linkedList.show()
    # linkedList.insert_nth(10, 5)
    # linkedList.insert_nth(11, 0)
    # linkedList.show()

