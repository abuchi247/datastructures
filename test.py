# 1 -> 2 -> 3 -> 4 -> null
# 1 -> 2 -> 3 -> 4 -> 5 -> null

class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def display(self):
        cur = self.head

        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

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

        return self.count_rec_1(first.next, count + 1)

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
                if self.head is None:  # if we don't have any elements in the list
                    self.tail = None
            else:
                prev.next = cur.next
                if cur.next is None:
                    self.tail = prev
            self.size -= 1


def front_back_split(source, front, back):
    if source.size < 2:
        front.head = source.head
        back.head = None
        return
    if source.size == 2:
        front.head = source.head
        back.head = source.head.next
        front.head.next = None
        return

    temp = None
    fast = source.head
    slow = source.head

    while fast is not None:
        fast = fast.next

        # check if fast is None
        if fast is None:
            break

        # move the fast pointer again
        fast = fast.next

        # check if fast is None again
        if fast is not None:
            temp = slow
            slow = slow.next

    front.head = source.head
    back.head = slow.next
    temp.next.next = None


def remove_duplicate(source):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    if source.head is None:
        return

    cur = source.head
    while cur.next is not None:
        temp = cur
        while cur.data == temp.data:
            temp = temp.next
        cur.next = temp
        cur = cur.next


# def alternate_split(source, aref, bref):
#     if source.head is None: return
#     if source.size <= 2:
#         aref.head = source.head
#         bref.head = source.head.next
#         aref.head.next = None
#
#     aref.head = source.head
#     prev = aref.head
#     afast = source.head
#
#     while afast is not None:
#         afast = afast.next
#         if afast is None:
#             break
#
#         afast = afast.next
#         if afast is not None:
#             prev.next = afast
#             prev = prev.next
#
#     bref.head = source.head.next
#     prevb = bref.head
#     bfast = source.head.next
#
#     while bfast is not None:
#         bfast = bfast.next
#         if bfast is None:
#             break
#
#         bfast = bfast.next
#         if bfast is not None:
#             prevb.next = bfast
#             prevb = prevb.next

def alternate_split(source, aref, bref):
    if source.head is None: return
    if source.size <= 2:
        aref.head = source.head
        bref.head = source.head.next
        aref.head.next = None

    list1 = source.head
    list1Temp = list1
    list2 = source.head.next
    list2Temp = list2

    while list2 is not None and list2.next is not None:
        if list1Temp is not None:
            if list1Temp.next is not None:
                list1Temp.next = list2Temp.next
            list1Temp = list1Temp.next
        if list2Temp is not None:
            if list2Temp.next is not None:
                list2Temp.next = list1Temp.next
            list2Temp = list2Temp.next

    aref.head = list1
    bref.head = list2


if __name__ == "__main__":
    source = SinglyLinkedList()
    source.append(1)
    source.append(2)
    source.append(3)
    source.append(4)
    # source.append(5)
    # source.append(6)
    source.display()

    # front = SinglyLinkedList()
    # back = SinglyLinkedList()
    #
    # front_back_split(source, front, back)
    # front.display()
    # back.display()
    # remove_duplicate(source)
    aref = SinglyLinkedList()
    bref = SinglyLinkedList()
    alternate_split(source, aref, bref)
    aref.display()
    bref.display()
