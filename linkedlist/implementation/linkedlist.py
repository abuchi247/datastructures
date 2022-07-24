class Node:
    """
    Implements the node of a linked list data structure
    """
    __slots__ = "data", "next"

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    implements the singly linked list
    """
    def __init__(self):
        self.head = None

    def traverse(self):
        """
        traverse through a linked list using the head node as a starting point
        :param head: head node of the linked list
        :return:
        """
        head = self.head
        print("[", end="")
        while head is not None:
            print(head.data, end=" -> ")
            head = head.next
        print("None]")

    def get_length(self):
        """
        Gets the length of a linked list
        :param head: head node of the linked list
        :return:   length of the linked list

        Big O(n) -> we have to iterate to the end of the linked list to get the size
        """
        length = 0  # initialize the length with 0
        # while there's a node in the linked list do the below

        head = self.head
        while head is not None:
            length += 1 # increment length
            head = head.next

        return length

    def get_nth(self, nth):
        """
        Gets the nth element in the linked list
        :param nth: nth position
        :return: the node at nth position

        Big O(n) -> worst case we query for an index not in the linked list
        """
        # if nth is None invalid entry
        if nth is None:
            raise TypeError("nth cannot be None")

        # if nth is < 0 invalid position
        if nth < 0:
            return None

        index = 0
        head = self.head
        while head is not None and index < nth:
            index += 1
            head = head.next

        return head # return the node

    def append_data(self, data):
        """
        Appends the data to the end of a linked list
        :param head:    head reference of the linked list
        :param data:    data to be added to the end of the linked list
        :return:    None

        Big O(n) -> since we are adding an element to the end of a linked list
        """
        new_node = Node(data)   # creating a node for the new data

        if self.head is None:
            self.head = new_node
        else:
            head = self.head
            # iterate until we get to the last element before None
            while head.next is not None:
                head = head.next
            head.next = new_node    # make the last node point to the new node
        return


    def pop(self):
        """
        Using a linked list as a stack. we need to pop the very first element in the linked list

        big O(1) -> constant time because we are popping the first element at the head of the linked list
        :param head:   head node
        :return:    data of the element that was popped
        """

        # verify the linked list is not empty
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next
        return data


    def delete_list(self):
        """
        Deletes all the elements in a linked list

        Big O(N) linear time as it removes the entire elements in the linked list
        :return:
        """

        while self.head is not None:
            print(f"Freeing: {self.head.data}")
            next = self.head.next   # get the value of the next pointer
            self.head.next = None   # set the next pointer to None
            self.head = next        # set head to the next pointer

    def insert_nth(self, data, nth):
        """
        Inserts data at the nth position in the linked list

        Rules:
            if nth is greater than the list, append to the end

        Big O(N) if the data is to be inserted at the tail of the linked list
        :param data:
        :param nth:
        :return:
        """

        if nth < 0:
            raise Exception(f"nth: {nth} is less than 0")

        prev = None
        cur = self.head
        new_node = Node(data)   # new node to be inserted
        index = 0

        while cur is not None and index != nth:
            prev = cur  # keeps track of the previous position
            cur = cur.next  # keeps track of the current position
            index += 1      # keeps track of the position

        # # nth is greater than the available index
        # if nth > index:
        #     raise Exception(f"nth: {nth} is out of bound")

        # inserting to the head node
        if prev is None:
            new_node.next = cur
            self.head = new_node
        else:
            prev.next = new_node
            new_node.next = cur
        return

    def sorted_insert(self, data):
        """
        Inserts a data into a sorted linked list in the right position

        Big O(n) -> could be at the tail of the linked list
        :param data:   data to be inserted
        :return:
        """
        # we have data in the linked list
        prev = None
        cur = self.head

        while cur is not None and data > cur.data:
            prev = cur
            cur = cur.next

        new_node = Node(data)

        # the data should be at the head
        if prev is None:
            self.head = new_node
        else:   # point the prev to the new node
            prev.next = new_node

        # point the new point to the next element
        new_node.next = cur
        return


def append_second_list(lista, listb):
    """
    This function appends listb to the end of lista
    :param list1:
    :param list2:
    :return:
    """

    if lista.head is None and listb.head is None:
        return

    prev = None
    cur = lista.head

    while cur is not None:
        prev = cur
        cur = cur.next

    # if list A head is Null
    if prev is None:
        lista.head = listb.head
    else:   # Point the last element of list A to Null
        prev.next = listb.head
    listb.head = None   # point list B head to Null
    return


def front_back_split_suboptimal(source, front_ref, back_ref):
    """
    This function splits the source list into 2 lists

    example: 1 -> 2 -> 3 -> 4 -> 5 -> None
    becomes: 1 -> 2 -> 3 -> None
             4 -> 5 -> None

    Big O(N) -> Algorithm
    :param source:
    :param front_ref:
    :param back_ref:
    :return:
    """

    if source.head is None:
        return front_ref, back_ref

    num_of_elements = 0
    current = source.head

    while current is not None:
        num_of_elements += 1
        current = current.next

    mid_point = num_of_elements // 2    # get the midpoint
    prev = source.head
    current = prev.next
    front_ref.head = prev
    index = 0

    while index < mid_point:
        prev = prev.next
        current = current.next
        index += 1

    prev.next = None

    back_ref.head = current
    return front_ref, back_ref


def front_back_split_optimal(source, front_ref, back_ref):
    """
    This function splits the source list into 2 lists

    example: 1 -> 2 -> 3 -> 4 -> 5 -> None
    becomes: 1 -> 2 -> 3 -> None
             4 -> 5 -> None

    Big O(N) -> Algorithm
    :param source:
    :param front_ref:
    :param back_ref:
    :return:
    """
    # if source is empty
    if source.head is None:
        return front_ref, back_ref

    # if source has only one element
    if source.head.next is None:
        front_ref.head = source.head
        back_ref.head = None
        return front_ref, back_ref

    slow = source.head
    fast = source.head

    while fast is not None:
        fast = fast.next

        # check if fast is None
        if fast is None:
            break

        # move the fast pointer again
        fast = fast.next

        # check if fast is None again
        if fast is not None:
            slow = slow.next

    front_ref.head = source.head
    back_ref.head = slow.next
    # slow.next = None

    return front_ref, back_ref


def remove_duplicate(source):
    """
    Removes duplicate elements from a sorted linked list
    :param source:
    :return:
    """
    # if linked list is empty
    if source.head is None:
        return

    # we have at least one element
    cur = source.head.next  # points to the second element
    prev = source.head  # points to the first element

    while cur is not None:
        if cur is not None and prev.data == cur.data:
            prev.next = cur.next
            cur.next = None
            cur = prev.next
            continue
        prev = cur
        cur = cur.next
    return


def move_node(source_ref, dest_ref):
    """
    Moves the head node from source to the head node in dest ref

    example:
        source => 1->2->3->None
        dest   => 4->5->6->None
        After move_node
        source => 2->3->None
        dest   => 1->4->5->6->None
    :param source_ref:
    :param dest_ref:
    :return:
    """
    # if the source is None, then no action needs to be performed
    if source_ref.head is None:
        return

    node_to_move = source_ref.head
    source_ref.head = source_ref.head.next

    node_to_move.next = dest_ref.head
    dest_ref.head = node_to_move


def sorted_merge(a, b):
    """
    Merge linked lists a and b into one sorted linked list

    a => 0->2->4->6->None
    b   => 1->2->3->5->None
    output => 0->1->2->2->3->4->5->6->None

    :param a:
    :param b:
    :return:
    """
    a_cur = a.head
    b_cur = b.head

    # if one of the 2 linked lists is empty
    if a_cur is None:
        return b_cur

    if b_cur is None:
        return a_cur

    # figure out which not to put first on the merged linked list
    if a_cur.data < b_cur.data:
        head = a_cur    # insert b to the merged linked list
        a_cur = a_cur.next  # move b pointer forward
    else:
        head = b_cur    # insert a as the first node in the merged linked list
        b_cur = b_cur.next

    head.next = None    # set head's next point to null

    curr = head

    while a_cur is not None and b_cur is not None:
        if a_cur.data < b_cur.data:
            curr.next = a_cur
            a_cur = a_cur.next
        else:
            curr.next = b_cur
            b_cur = b_cur.next

        curr = curr.next  # go on to the next node

    # ensure everything this is added to the merged linked list
    if a_cur is not None:
        curr.next = a_cur
    else:
        curr.next = b_cur

    return head


def reverse(mylist):
    """
    reverse a linked list
    :param source:
    :return:
    """
    if mylist.head is None:
        return None

    curr = mylist.head
    prev = None

    while curr is not None:
        next = curr.next    # to store the next element current is pointing to
        curr.next = prev    # make the cur next point to point to prev element
        prev = curr         # move prev to curr position
        curr = next # move curr to the next curr node

    return prev


if __name__ == "__main__":
    list1 = LinkedList()
    list1.append_data(1)
    list1.append_data(2)
    list1.append_data(3)

    print(f"List size: {list1.get_length()}")

    # test the get nth function
    for nth in range(5):
        print(f"nth: {nth} -> {list1.get_nth(nth).data if list1.get_nth(nth) else list1.get_nth(nth)}")
    print()

    list1.append_data(4)

    # test the get nth function
    for nth in range(5):
        print(f"nth: {nth} -> {list1.get_nth(nth).data if list1.get_nth(nth) else list1.get_nth(nth)}")
    print()

    # # test popping element      1 -> 2 -> 3 -> 4
    print(f"Data popped: {list1.pop()}")

    list1.traverse()

    list1.insert_nth(0, 3)

    list1.traverse()

    list1.delete_list()

    list1.sorted_insert(1)
    list1.sorted_insert(3)
    list1.sorted_insert(5)
    list1.sorted_insert(7)
    list1.sorted_insert(4)
    list1.traverse()

    lista = LinkedList()
    listb = LinkedList()
    lista.append_data(1)
    lista.append_data(5)
    lista.append_data(7)

    listb.append_data(4)
    listb.append_data(6)
    listb.append_data(8)

    lista.traverse()
    listb.traverse()

    append_second_list(lista, listb)

    lista.append_data(10)
    listb.append_data(11)

    lista.traverse()
    listb.traverse()

    front_ref = LinkedList()
    back_ref = LinkedList()

    front_ref, back_ref = front_back_split_optimal(lista, front_ref, back_ref)

    front_ref.traverse()
    back_ref.traverse()

    listc = LinkedList()
    listc.append_data(2)
    listc.append_data(2)
    listc.append_data(3)
    listc.append_data(3)
    listc.append_data(3)
    listc.append_data(4)
    listc.append_data(4)

    remove_duplicate(listc)
    listc.traverse()

    source_ref = LinkedList()
    dest_ref = LinkedList()

    source_ref.append_data(0)
    source_ref.append_data(1)
    source_ref.append_data(2)
    source_ref.traverse()

    dest_ref.append_data(4)
    dest_ref.append_data(5)
    dest_ref.append_data(6)
    dest_ref.traverse()

    move_node(source_ref, dest_ref)
    source_ref.traverse()
    dest_ref.traverse()

    a_list = LinkedList()
    b_list = LinkedList()
    a_list.append_data(0)
    a_list.append_data(2)
    a_list.append_data(4)
    a_list.append_data(6)
    b_list.append_data(1)
    b_list.append_data(3)
    b_list.append_data(5)
    b_list.append_data(7)
    print("Before merging linked list")
    print("A list")
    a_list.traverse()
    print("B list")
    b_list.traverse()

    merged_result = sorted_merge(a_list, b_list)
    merged_list = LinkedList()
    merged_list.head = merged_result
    print("Sorted merged linked list result")
    merged_list.traverse()

    print("Reversd linked list of above")
    reversed_list = LinkedList()
    reversed_list.head = reverse(merged_list)
    reversed_list.traverse()