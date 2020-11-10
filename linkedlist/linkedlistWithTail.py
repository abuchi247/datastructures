class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_length(self):
        return self.size

    def is_empty(self):
        return self.size == 0 

    def prepend(self, data):
        """
        Big O(1)
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return

    def append(self, data):
        """
        Big O(1)
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return

    def search(self, data):
        """
        Big O(N)
        """
        curr = self.head

        while curr is not None and curr.data != data:
            curr = curr.next
        
        return curr

    def traverse_to_index(self, index):
        """
        Big O(N)
        """
        count = 0
        curr = self.head

        while curr is not None and count != index:
            curr = curr.next
            count += 1

        return curr


    def insert(self, nth, data):
        """
        Big O(N)
        """
        
        if nth <= 0:
            return self.prepend(data)

        elif nth >= self.get_length():
            return self.append(data)

        # insert in the middle
        new_node = Node(data)
        prev = self.traverse_to_index(nth - 1)
        next_node = prev.next
        prev.next = new_node
        new_node.next = next_node

        self.size += 1
        return


    def delete(self, data):
        """
        Big O(N)
        """
        prev = None
        curr = self.head

        if self.is_empty():
            return None

        while curr is not None and curr.data != data:
            prev = curr
            curr = curr.next

        if curr is None:
            return None
        
        if prev is None:
            self.head = curr.next

            if self.head is None:
                self.tail = self.head
        else:
            prev.next = curr.next
            if self.tail == curr:
                self.tail = prev
        self.size -= 1
        return



    def print_list(self):
        leader = self.head
        while leader is not None:
            print(leader.data, end=" -> ")
            leader = leader.next
        print("None")


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.prepend(20)
    mylist.prepend(10)
    mylist.append(10)

    print(mylist.search(10))

    print("Before")
    mylist.print_list()
    mylist.insert(0, 5)
    mylist.insert(20, 50)
    print("After")
    mylist.print_list()
    print(mylist.head.data, mylist.tail.data)
    print("Size:", mylist.get_length())

    print("After Delete")
    mylist.delete(50)
    mylist.print_list()
    print(mylist.head.data, mylist.tail.data)
    print("Size:", mylist.get_length())