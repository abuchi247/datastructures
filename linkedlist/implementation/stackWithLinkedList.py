import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data


class StackEmptyException(Exception):
    pass


class StackWithLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise StackEmptyException("Stack is empty")
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("Stack is empty")
        data = self.top.data
        next_head = self.top.next
        self.top.next = None
        self.top = next_head
        self.size -= 1
        return data

    def display(self):
        cur = self.top
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def delete_all(self):
        while self.top is not None:
            print(f"Freeing: {self.top.data}")
            next = self.top.next
            self.top.next = None
            del self.top
            self.top = next

    def insert_nth(self, data, nth):
        new_node = Node(data)
        index = 0
        prev = None
        cur = self.top

        while cur is not None and index < nth:
            prev = cur
            cur = cur.next
            index += 1
        # insert at the beginning
        if prev is None:
            self.top = new_node
        else:
            prev.next = new_node
        new_node.next = cur
        self.size += 1

    def insert_sorted(self, data):
        new_node = Node(data)
        prev = None
        cur = self.top

        while cur is not None and cur.data < data:
            prev = cur
            cur = cur.next

        if prev is None:
            self.top = new_node
        else:
            prev.next = new_node
        new_node.next = cur


    def remove_duplicates(self):
        if self.is_empty():
            return

        prev = self.top
        cur = self.top.next

        while cur is not None:
            if prev.data == cur.data:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
                continue
            prev = cur
            cur = cur.next

def merge_sorted_list(lista, listb):
    if lista is None: return listb
    if listb is None: return lista

    if lista.data < listb.data:
        head = lista
        lista = lista.next
    else:
        head = listb
        listb = listb.next

    head.next = None
    cur = head
    while lista is not None and listb is not None:
        if lista.data < listb.data:
            cur.next = lista
            lista = lista.next

        else:
            cur.next = listb
            listb = listb.next
        cur = cur.next

    if lista is not None:
        cur.next = lista
    else:
        cur.next = listb

    return head


def reverse_iter(head):
    prev = None
    cur = head

    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


if __name__ == "__main__":
    s = StackWithLinkedList()
    # s.display()
    # s.push(3)
    # s.push(4)
    # s.push(5)
    # s.display()
    # s.pop()
    # s.display()
    # s.pop()
    # s.display()
    # s.push(2)
    # s.display()
    #
    # for x in range(10):
    #     s.push(x**2)
    #
    # s.display()
    # s.delete_all()
    # print(s.top)
    # s.display()
    #
    # s.insert_nth(1, 5)
    # s.display()
    # s.insert_nth(2, 11)
    # s.display()
    # s.insert_nth(2, -11)
    # s.display()
    # s.insert_nth(20, 1)
    # s.display()
    # s.insert_nth(50, 3)
    # s.display()

    # s.insert_sorted(4)
    # s.display()
    # s.insert_sorted(10)
    # s.display()
    # s.insert_sorted(2)
    # s.display()
    # s.insert_sorted(5)
    # s.display()
    # s.insert_sorted(20)
    # s.display()
    # s.push(1)
    # s.push(1)
    # # s.insert_nth(2, 33)
    # # s.insert_nth(2, 33)
    # # s.insert_nth(2, 33)
    # # s.insert_nth(3, 33)
    # s.remove_duplicates()
    # s.display()
    s.insert_sorted(1)
    s.insert_sorted(3)
    s.insert_sorted(5)
    s.display()

    v = StackWithLinkedList()
    v.insert_sorted(2)
    v.insert_sorted(4)
    v.insert_sorted(6)
    v.display()

    final = merge_sorted_list(s.top, v.top)
    #
    # while final is not None:
    #     print(final.data, sep=" -> ")
    #     final = final.next

    final = reverse_iter(final)
    while final is not None:
        print(final.data, sep=" -> ")
        final = final.next

