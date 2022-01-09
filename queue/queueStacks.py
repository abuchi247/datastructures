class QueueStack:

    def __init__(self):
        self.forward_stack = []
        self.reverse_stack = []

    def is_empty(self):
        return len(self.forward_stack) == 0 and len(self.reverse_stack) == 0

    def enqueue(self, value):
        while len(self.reverse_stack) > 0:
            self.forward_stack.append(self.reverse_stack.pop())
        self.forward_stack.append(value)

    def dequeue(self):
        while len(self.forward_stack) > 0:
            self.reverse_stack.append(self.forward_stack.pop())
        return self.reverse_stack.pop()

    def display(self):
        while len(self.reverse_stack) > 0:
            self.forward_stack.append(self.reverse_stack.pop())
        print(self.forward_stack)


if __name__ == "__main__":
    q = QueueStack()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    print(q.dequeue())
    q.enqueue(4)
    q.display()
    q.dequeue()
    q.display()