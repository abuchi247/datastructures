class Node:
    __slots__ = "element", "next"

    def __init__(self, element, next=None):
        self.element = element
        self.next = next


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_length(self):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        :return:
        """
        # length = 0
        # while head is not None:
        #     length += 1
        #     head = head.next
        # return length
        return self.size

    def is_empty(self):
        """
        Time complexity: O(1)
        :return:
        """
        return self.head is None

    @staticmethod
    def get_nth(head, n):
        """
        Returns the node element at the index n
        Time complexity: O(n)
        Space complexity: O(1)
        :param head:
        :param n:
        :return:
        """
        # edge cases
        if head is None:
            return None

        # check if n is valid
        if n < 0:
            # print("Invalid index")
            return None

        index = 0
        while head is not None:
            if index == n:
                return head.element
            index += 1
            head = head.next

        # if we get here that means n (index) is greater than the length of the list
        # print("Index out of bound")
        return None

    def add_last(self, data):
        """
        This function appends a data to the end of the linked list
        Time complexity: O(n) - slow
        Time complexity: O(1) - fast solution
        Space complexity: O(1)
        :param head:
        :param data:
        :return:
        """
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        # we have at least one node in the linkedlist
        # current = self.head
        # while current.next is not None:
        #     current = current.next
        #
        # # we should be at the end of the list
        # current.next = new_node
        self.tail.next = new_node
        self.tail = new_node
        return

    def add_first(self, data):
        new_node = Node(data)
        self.size += 1
        # if list is empty
        if self.is_empty():
            self.head = self.tail = new_node
            return
        # list is not empty
        new_node.next = self.head
        self.head = new_node
        return

    def traverse(self):
        """
        Time complexity: O(n)
        Space complexity: O(1)
        :return:
        """
        current = self.head

        while current is not None:
            print(current.element, end=" -> ")
            current = current.next
        print("Null")

    def pop(self):
        """
        Time complexity: O(n) - slow solution
        Time complexity: O(1) - fast solution
        Space complexity: O(1)
        :return:
        """
        if self.is_empty():
            return None

        data = self.head.element
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return data

    def delete_list(self):
        """
        Deletes all the elements in the list
        Time complexity: O(1)
        :return:
        """
        if not self.is_empty():
            self.head = self.tail = None
            self.size = 0
        return

    def insert_nth(self, data, nth):
        """
        Insert data to the nth position
        Time complexity: O(n)
        :param data:
        :param nth:
        :return:
        """
        if nth < 0:
            print("out of bound")
            return

        new_node = Node(data)
        index = 0
        curr = self.head
        prev = None

        while index < nth and curr != None:
            prev = curr
            curr = curr.next
            index += 1

        if index == 0:
            new_node.next = curr
            self.head = new_node
        else:
            prev.next = new_node
            new_node.next = curr
            if curr is None:
                self.tail = new_node
        self.size += 1
        return

    def sorted_insert(self, data):
        new_node = Node(data)

        curr = self.head
        prev = None
        while curr is not None and data > curr.element:
            prev = curr
            curr = curr.next

        if prev is not None:
            prev.next = new_node
        else:
            self.head = new_node
        new_node.next = curr
        self.size += 1
        return


def traverse(head):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    :return:
    """
    current = head

    while current is not None:
        print(current.element, end=" -> ")
        current = current.next
    print("Null")


def append_second_list(a, b):
    if a is None:
        a = b
        b = None
        return

    curr = a
    while curr.next is not None:
        curr = curr.next

    curr.next = b
    b = None
    return


def front_back_split(source, front_ref, back_ref):
    pass


if __name__ == "__main__":
    mylist = SinglyLinkedList()
    # mylist.add_last(4)
    # mylist.add_last(5)
    # mylist.add_last(6)
    # mylist.traverse()
    # print(mylist.get_length())
    # print(mylist.get_nth(mylist.head, 4))
    # print(mylist.get_nth(mylist.head, 1))
    # print(mylist.get_nth(mylist.head, -1))
    # print(mylist.get_nth(mylist.head, 0))
    # mylist.add_first(10)
    # print(mylist.pop())
    # mylist.traverse()
    # # mylist.delete_list()
    # mylist.traverse()  # 4 -> 5 -> 6 -> Null
    # mylist.insert_nth(3, 0)
    # mylist.traverse()  # 3 -> 4 -> 5 -> 6 -> Null
    # mylist.insert_nth(9, 4)
    # mylist.traverse()   # 3 -> 4 -> 5 -> 6 -> 9 -> Null
    # mylist.insert_nth(10, 1)
    # mylist.traverse()   # 3 -> 10 -> 4 -> 5 -> 6 -> 9 -> Null
    # print(mylist.head.element)  # 3
    # print(mylist.tail.element)  # 9
    mylist.sorted_insert(1)
    mylist.sorted_insert(2)
    mylist.sorted_insert(1)
    mylist.traverse()
    mylist.sorted_insert(6)
    # mylist.sorted_insert(10)
    # print(mylist.head.next.next.element)
    mylist.traverse()

    mylist2 = SinglyLinkedList()
    mylist2.add_first(3)
    mylist2.add_first(8)
    mylist2.add_first(2)

    # traverse(mylist2.head)
    append_second_list(mylist.head, mylist2.head)
    traverse(mylist.head)
    # traverse(mylist2.head)

    front, back = front_back_split(mylist.head, None, None)
    traverse(front)
    traverse(back)