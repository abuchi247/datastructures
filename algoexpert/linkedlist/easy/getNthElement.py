from singlyLinkedList import SinglyLinkedList, Node


def get_nth(head, nth):
    """
    Get the nth element in a linkedlist

    Time complexity: O(N)
    Space complexity: O(1)
    """
    if nth < 0:
        return None

    cur = head
    index = 0
    while cur is not None and index < nth:
        index += 1
        cur = cur.get_next()

    return cur


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    print(f"get the {-1}th element in the linked list: {get_nth(linkedList.head, -1)}")
    linkedList.append(12)
    linkedList.append(0)
    linkedList.append(2)
    print(f"get the {10}th element in the linked list: {get_nth(linkedList.head, 10)}")
    print(f"get the {0}th element in the linked list: {get_nth(linkedList.head, 0)}")
    print(f"get the {1}th element in the linked list: {get_nth(linkedList.head, 1)}")
    print(f"get the {2}th element in the linked list: {get_nth(linkedList.head, 2)}")
    linkedList.pop_first()
    print(f"get the {0}th element in the linked list: {get_nth(linkedList.head, 0)}")
