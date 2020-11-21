class Node:
    __slots__ = "data", "next"

    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    """
    First In First Out -> FIFO data structure

    Operations:
    enqueue(item) -> add item to the tail of a queue
    dequeue() -> remove the first item from the queue
    is_empty() -> check if a queue is empty or not
    front() -> returns the first item in a queue without removing it from the queue
    get_length() -> returns the number of items in a queue
    """

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def get_length(self):
        """
        Gets the size of the queue

        Big O(1)
        """
        return self.size

    def is_empty(self):
        """
        Checks if a queue is empty or not

        Big O(1)
        """
        return self.first is None

    def front(self):
        """
        Gets the first item in a queue without removing it from the queue

        Big O(1)
        """
        if self.is_empty():
            print("Queue is empty")
            return
        return self.first

    def dequeue(self):
        """
        Removes the first item in the queue

        Big O(1)
        """
        if self.is_empty():
            print("Queue is empty")
            return
        
        item_removed = self.first # get the first item
        self.first = self.first.next    # set first to be the next item to first

        # Come here if the queue had only one item before
        if self.first is None:
            self.last = None

        self.size -= 1
        return item_removed

    def enqueue(self, item):
        """
        Adds an item to the end of the queue

        Big O(1)
        """
        new_node = Node(item)   # create a node for item
        
        if self.is_empty(): # if queue was empty
            self.first = self.last = new_node
        else:
            self.last.next = new_node   # point the old last to the new node
            self.last = new_node    # set the last node to be the new node
        self.size += 1
        return

    def print_all(self):
        """
        Prints all the items in a queue

        Big O(N)
        """
        print("[FRONT]", end=" <- ")
        cur = self.first

        while cur is not None:
            print(cur.data, end=" <- ")
            cur = cur.next
        print("[BACK]")


if __name__ == "__main__":
    queue = QueueLinkedList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("After enqueue")
    queue.print_all()
    print("Queue size: ", queue.get_length())
    print("Firt Item: ", queue.front().data)
    print("Removed first item ", queue.dequeue().data)
    print("first item ", queue.front().data)
    queue.print_all()
    print("Queue size: ", queue.get_length())
    print("Adding again")
    queue.enqueue(100)
    queue.print_all()