class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @staticmethod
    def display_iter(first):
        cur = first

        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    @classmethod
    def display_rec(cls, first):
        """
        Time complexity: O(N)
        Space complexity: O(N)
            calls: N+1 times
            space: N+1 times
        """
        if first is None:
            return
        print(first.data, end=" ")
        cls.display_rec(first.next)

    def count_opt(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        return self.size

    def count_iter(self):
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def count_rec_1(self, first, count=0):
        """
        Time complexity: O(N)
        Space complexity: 0(N)
            calls: N+1 times
            space: N+1 times
        """
        if first is None:
            return count

        return self.count_rec_1(first.next, count+1)

    def count_rec_2(self, first):
        """
        Time complexity: O(N)
        Space complexity: 0(N)
            calls: N+1 times
            space: N+1 times
        """
        if first is None:
            return 0

        return self.count_rec_2(first.next) + 1

    def append(self, data):
        """
        Appends a node to the tail of the linked list
        :param: data: data to be added

        Time complexity: O(1)
        Space complexity: O(1)
        """
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, nth, data):
        """
        Insert a data to the nth position in the linked list
        :param: nth: index to insert data
        :param: data: data to be insert

        Time complexity: O(N)
        Space complexity: O(1)
        """
        if nth < 0:
            raise Exception(f"Index cannot be less than 0")

        index = 0
        prev = None
        cur = self.head
        new_node = Node(data)

        while cur is not None and index != nth:
            prev = cur
            cur = cur.next
            index += 1

        if prev is None:
            new_node.next = cur

            if self.head is None:
                self.head = self.tail = new_node
            else:
                self.head = new_node
        else:
            prev.next = new_node
            new_node.next = cur

            # if we are inserting to the last, set that to tail
            if cur is None:
                self.tail = new_node
        self.size += 1

    def insert_last(self, value):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_sorted(self, data):
        """
        Insert node in a sorted order
        Time complexity: O(N)
        Space complexity: O(1)
        """
        new_node = Node(data)
        prev = None
        cur = self.head

        while cur is not None and cur.data < data:
            prev = cur
            cur = cur.next

        if prev is None:
            new_node.next = self.head

            if self.head is None:
                self.head = self.tail = new_node
            else:
                self.head = new_node
        else:
            prev.next = new_node
            new_node.next = cur

            if cur is None:
                self.tail = new_node
        self.size += 1

    def delete(self, data):
        """
        Delete the data from the linked list
        Time complexity: O(N)
        Space complexity: O(1)
        """
        prev = None
        cur = self.head

        while cur is not None and cur.data != data:
            prev = cur
            cur = cur.next

        if cur is None:
            print("Not found")
        else:
            # deleting the first element
            if prev is None:
                self.head = self.head.next
                if self.head is None: # if we don't have any elements in the list
                    self.tail = None
            else:
                prev.next = cur.next
                if cur.next is None:
                    self.tail = prev
            self.size -= 1

    def is_sorted(self):
        """
        Checks if the linked list is sorted or not
        :returns True if sorted otherwise, False
        """
        if self.head is None or self.head == self.tail:
            return True

        prev = self.head
        cur = self.head.next

        while cur is not None:
            if prev.data > cur.data:
                return False
            prev = cur
            cur = cur.next
        return True

    def remove_duplicate(self):
        """
        Removes duplicate elements from a sorted linkedlist

        Time complexity: O(N)
        Space complexity: O(1)
        """
        count = 0
        prev = None
        cur = self.head

        while cur is not None:
            prev = cur
            cur = cur.next

            while cur is not None and prev.data == cur.data:
                next = cur.next
                cur.next = None     # unlinking node
                cur = next
            prev.next = cur
            count += 1
        self.size = count
        self.tail = prev

    def reverse_iter(self):
        """
        Reverse the linked list by reversing links
        Time complexity: O(N)
        Space complexity: O(1)
        """
        prev = None
        cur = self.head
        self.tail = cur
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def reverse_iter_slow(self):
        """
        Reverse the linked list by reversing elements
        Time complexity: O(N)
        Space complexity: O(N)
        """
        A = [0]*self.size
        cur = self.head
        index = 0
        while cur is not None:
            A[index] = cur.data
            index += 1
            cur = cur.next

        # copy the elements in the array to the linked list
        cur = self.head
        while cur is not None:
            cur.data = A[index - 1]
            index -= 1
            cur = cur.next

    def reverse_rec(self, cur):
        """
        Reverse a linked list
        Time complexity: O(N)
        Space complexity: O(N)
            calls: N+1 times
            space: N+1 times
        """
        if cur is None:
            return

        if cur.next is None:
            self.head = cur
            return

        self.reverse_rec(cur.next)
        cur.next.next = cur
        cur.next = None
        self.tail = cur


def sum_nodes_iter(head):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    total = 0
    cur = head
    while cur is not None:
        total += cur.data
        cur = cur.next
    return total


def sum_nodes_rec1(head):
    """
    Time complexity: O(N)
    Space complexity: O(N)
        calls: N+1
        space: N+1
    """
    if head is None:
        return 0
    return head.data + sum_nodes_rec1(head.next)


def find_max_iter(head):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    max_value = 0
    cur = head

    while cur is not None:
        if cur.data > max_value:
            max_value = cur.data
        cur = cur.next
    return max_value


def find_max_rec(first, max_value=0):
    if first is None:
        return max_value

    if first.data > max_value:
        max_value = first.data
    return find_max_rec(first.next, max_value)


def search_iter(head, target):
    cur = head
    while cur is not None:
        if cur.data == target:
            return cur
        cur = cur.next
    return None


def search_rec(head, target):
    if head is None:
        return None

    if head.data == target:
        return head
    return search_iter(head.next, target)


def concatenate_list(a_head, b_head):
    new_head = None
    new_tail = None

    # adding first list
    while a_head is not None:
        if new_tail is None and new_tail is None:
            new_head = new_tail = a_head
        else:
            new_tail.next = a_head
            new_tail = a_head
        next = a_head.next
        a_head.next = None
        a_head = next

    #   add the second list
    while b_head is not None:
        if new_tail is None and new_tail is None:
            new_tail = new_tail = b_head
        else:
            new_tail.next = b_head
            new_tail = b_head
        next = b_head.next
        b_head.next = None
        b_head = next

    return new_head


if __name__ == "__main__":
    A = [10, 2, 3, 4, 5, 0]
    my_list = SinglyLinkedList()
    # for num in A:
    #     my_list.append(num)
    #
    # # my_list.display_iter(my_list.head)
    # my_list.display_rec(my_list.head)
    #
    # print()
    # print(f"count: {my_list.count_iter()}")
    # print(f"count: {my_list.count_rec_1(my_list.head)}")
    # print(f"count: {my_list.count_rec_2(my_list.head)}")
    # print(f"sum of nodes: {sum_nodes_iter(my_list.head)}")
    # print(f"sum of nodes: {sum_nodes_rec1(my_list.head)}")
    # print(f"Max element: {find_max_iter(my_list.head)}")
    # print(f"Max element: {find_max_rec(my_list.head)}")
    # print(f"Search iter: {search_iter(my_list.head, 10)}")
    # print(f"Search rec: {search_rec(my_list.head, 10)}")
    # my_list.display_iter(my_list.head)
    # my_list.insert(8, 20)
    # print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    # # my_list.insert(0, 21)
    # print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    # my_list.insert(4, 22)
    # print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    # my_list.insert(10, 25)
    # print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    # my_list.insert_last(50)
    # print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    # my_list.display_iter(my_list.head)
    #
    # my_list.append(1)
    # my_list.append(2)
    # my_list.insert_sorted(5)
    # my_list.append(3)
    # my_list.insert_sorted(4)
    # my_list.insert_sorted(3)
    # my_list.display_iter(my_list.head)
    # print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    my_list.insert(5, 12)
    my_list.insert(1, 2)
    my_list.insert(9, 3)
    my_list.insert_sorted(2)
    # my_list.insert_sorted(20)
    # my_list.delete(3)
    # # my_list.delete(22)
    # my_list.display_iter(my_list.head)
    # print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    # print(my_list.is_sorted())
    my_list.insert_sorted(2)
    my_list.insert_sorted(2)
    my_list.insert_sorted(3)
    my_list.insert_sorted(4)
    my_list.display_iter(my_list.head)
    print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    my_list.remove_duplicate()
    my_list.display_iter(my_list.head)
    print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")
    # my_list.reverse_iter()
    my_list.reverse_rec(my_list.head)
    # my_list.reverse_iter_slow()
    my_list.display_iter(my_list.head)
    print(f"head: {my_list.head.data}, tail: {my_list.tail.data}, size: {my_list.size}")

    concated_list = concatenate_list(my_list.head, None)
    SinglyLinkedList.display_iter(concated_list)
    SinglyLinkedList.display_iter(my_list.head)