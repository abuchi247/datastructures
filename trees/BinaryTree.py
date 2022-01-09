from StackLinkedList import StackLinkedList


class Queue:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            front_node = self.front
            if self.front == self.rear:
                self.rear = None
            self.front = self.front.next
            return front_node


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def get_user_input(question):
    while True:
        try:
            user_input = int(input(question))
            break
        except Exception:
            continue
    return user_input


def generate_tree():
    q = Queue()
    root_data = get_user_input("Enter the value for the root node: ")
    root_node = Node(root_data)
    q.enqueue(root_node)

    while not q.is_empty():
        cur_node = q.dequeue()
        left_data = get_user_input(f"Enter the value for the left child node for {cur_node.data.data} node: ")
        if left_data != -1:
            left_node = Node(left_data)
            cur_node.left_child = left_node
            q.enqueue(left_node)

        right_data = get_user_input(f"Enter the value for the right child node for {cur_node.data.data} node: ")
        if right_data != -1:
            right_node = Node(right_data)
            cur_node.right = right_node
            q.enqueue(right_node)

    return root_node


def pre_order(root_node):
    if root_node is None:
        return
    print(root_node.data)
    pre_order(root_node.left_child)
    pre_order(root_node.right_child)


def pre_order(root_node):
    s = StackLinkedList()
    t = root_node

    while t is not None or s.is_empty() != True:
        if t is not None:
            print(t.data)
            s.push(t)
            t = t.left_child
        else:
            t = s.pop()
            t = t.right_child




if __name__ == "__main__":
    root = generate_tree()
    pre_order(root)