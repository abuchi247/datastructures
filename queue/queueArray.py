class QueueArray:
    """
    First In First Out -> FIFO data structure

    Operations:
    enqueue(item) -> add item to the tail of a queue
    dequeue() -> remove the first item from the queue
    is_empty() -> check if a queue is empty or not
    front() -> returns the first item in a queue without removing it from the queue
    get_length() -> returns the number of items in a queue
    """

    MAX_CAPACITY = 10

    def __init__(self):
        self.data = [None] * self.MAX_CAPACITY
        self.first = -1
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
        return self.first == -1

    def is_full(self):
        """
        Check if the queue is full

        Big O(1)
        """
        return self.size == len(self.data)

    def front(self):
        """
        Gets the first item in a queue without removing it from the queue

        Big O(1)
        """
        if self.is_empty():
            print("Queue is empty")
            return
        return self.data[self.first]

    def dequeue(self):
        """
        Removes the first item in the queue

        Big O(1)
        """
        if self.is_empty():
            print("Queue is empty")
            return
        
        item_removed = self.data[self.first] # get the first item
        self.data[self.first] = None    # clear the item in that location
        self.first = (self.first + 1) % len(self.data)    # set first to be the next item to first

        self.size -= 1
        return item_removed

    def enqueue(self, item):
        """
        Adds an item to the end of the queue

        Big O(1)
        """
        if self.is_full():
            print("Queue is full")
            return
        
        if self.is_empty(): # if queue was empty
            self.first = (self.first + 1) % len(self.data)
            self.data[self.first] = item
        else:
            # [ None, None, 1, 2, 3, 4, 7, 9]
            avail = (self.first + self.size) % len(self.data) # get the location to insert new data
            self.data[avail] = item     # insert item in the available slot
        self.size += 1
        return

    def print_all(self):
        """
        Prints all the items in a queue

        Big O(N)
        """
        print("[FRONT]", end=" <- ")
        walker = self.first
        for i in range(self.size):
            pos = (walker + i) % len(self.data) # get the actual index in the data
            print(self.data[pos], end=" <- ")
        print("[BACK]")


if __name__ == "__main__":
    queue = QueueArray()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("After enqueue")
    queue.print_all()
    print("Queue size: ", queue.get_length())
    print("Firt Item: ", queue.front())
    print("Removed first item ", queue.dequeue())
    print("first item ", queue.front())
    queue.print_all()
    print("Queue size: ", queue.get_length())
    print("Adding again")
    queue.enqueue(100)
    queue.print_all()
    queue.dequeue()
    queue.enqueue(200)
    queue.print_all()
    print(queue.data)