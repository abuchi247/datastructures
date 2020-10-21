# Enter your code here. Read input from STDIN. Print output to STDOUT

# [G]
# while if queue is not empty
#  current_node = dequeue eleme
#
#   check if current_node.left is not None:
#           queue.enqueue(current_node.left) [R, X]
#   check if current_node.right is not None:
#           queue.enqueue(current_node.right)
# iter 1 -> [R, X]
# iteration 2
# [X, B, A,]
# iteration 2
# [B, A, C, S]

# G,O
# (R, 1) (X, 1)
# [(B, 2), (A,2), (C, S]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


class Tree:

    def __init__(self):
        self.head = None

    @staticmethod
    def connect_level_nodes(self, head):
        my_queue = []
        count = 0
        my_queue.append((head, count))

        while len(my_queue) > 0:
            current_node, count = my_queue.pop(0)

            if current_node.left != None:
                my_queue.append((current_node.left, count + 1))

            if current_node.right != None:
                my_queue.append((current_node.right, count + 1))

            if len(my_queue) > 0:
                if my_queue[0][1] == count:
                    current_node.next = my_queue[0][0]
