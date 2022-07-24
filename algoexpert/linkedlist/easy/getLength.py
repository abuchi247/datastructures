from singlyLinkedList import Node, SinglyLinkedList


def get_length(head):
    """
    Counts the number of elements in the linked list

    Time complexity: O(N)
    Space Complexity: O(1)
    """
    cur = head
    length = 0

    while cur is not None:
        length += 1
        cur = cur.get_next()

    return length


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    print(f"size of the linked list: {get_length(linkedList.head)}")
    linkedList.append(12)
    linkedList.append(0)
    linkedList.append(2)
    print(f"size of the linked list: {get_length(linkedList.head)}")
    linkedList.pop_first()
    print(f"size of the linked list: {get_length(linkedList.head)}")
    linkedList.delete_all()
    print(f"size of the linked list: {get_length(linkedList.head)}")
