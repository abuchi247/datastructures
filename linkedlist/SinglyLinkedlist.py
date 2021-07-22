class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def display_iter(first):
        cur = first

        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next

            cur.next = new_node

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

    def insert(self, nth, value):
        if nth < 0:
            print(f"Invalid index {nth}")
            return

        index = 0
        cur = self.head
        prev = None
        new_node = Node(value)

        while cur is not None and index != nth:
            index += 1
            prev = cur
            cur = cur.next

        if prev is None:
            new_node.next = self.head
            self.head = new_node
        else:
            prev.next = new_node
            new_node.next = cur


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


if __name__ == "__main__":
    A = [10, 2, 3, 4, 5, 0]
    my_list = SinglyLinkedList()
    for num in A:
        my_list.append(num)

    # my_list.display_iter(my_list.head)
    my_list.display_rec(my_list.head)

    print()
    print(f"count: {my_list.count_iter()}")
    print(f"count: {my_list.count_rec_1(my_list.head)}")
    print(f"count: {my_list.count_rec_2(my_list.head)}")
    print(f"sum of nodes: {sum_nodes_iter(my_list.head)}")
    print(f"sum of nodes: {sum_nodes_rec1(my_list.head)}")
    print(f"Max element: {find_max_iter(my_list.head)}")
    print(f"Max element: {find_max_rec(my_list.head)}")
    print(f"Search iter: {search_iter(my_list.head, 10)}")
    print(f"Search rec: {search_rec(my_list.head, 10)}")
    my_list.display_iter(my_list.head)
    my_list.insert(8, 20)
    my_list.insert(0, 21)
    my_list.insert(4, 22)
    my_list.insert(10, 25)
    my_list.display_iter(my_list.head)