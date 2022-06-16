# 1. build123()
# This is a very basic problem with a little pointer manipulation. (You can skip this problem if you are already
# comfortable with pointers.) Write code that builds the following little 1-2-3 binary search tree...
#   2
#  / \
#  1 3
# Write the code in three different ways...
# a: by calling newNode() three times, and using three pointer variables
# b: by calling newNode() three times, and using only one pointer variable
# c: by calling insert() three times passing it the root pointer to build up the tree

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def breadthFirstTraversal(node):
    queue = list()
    queue.append(node)

    while len(queue) > 0:
        cur = queue.pop(0)
        print(cur.data)

        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)


def insert_rec(node, data):
    if node is None:
        node = Node(data)
    else:
        if data <= node.data:
            node.left = insert_rec(node.left, data)
        else:
            node.right = insert_rec(node.right, data)
    return node


def insert_iter(root, data):
    if root is None:
        return Node(data)

    cur = root
    while cur is not None:
        if data <= cur.data:
            if cur.left is None:
                cur.left = Node(data)
                return
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = Node(data)
                return
            cur = cur.right
    return root


def build123():
    """
    Build tree using 3 pointers
    """
    root = Node(2)
    lChild = Node(1)
    rChild = Node(3)
    root.left = lChild
    root.right = rChild
    breadthFirstTraversal(root)


def build123_sol2():
    """
    Build tree using 1 pointers
    """
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    breadthFirstTraversal(root)


def build123_sol3():
    """
    Build tree using 1 pointers
    """
    root = insert_rec(None, 2)
    insert_iter(root, 1)
    insert_rec(root, 3)
    breadthFirstTraversal(root)


if __name__ == "__main__":
    build123()
    build123_sol2()
    build123_sol3()