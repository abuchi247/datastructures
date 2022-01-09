## Create a binary search tree using the following list
## Key: 9, 15, 5, 20, 16, 8, 12, 3, 6
                #             9
                #     5               15
                # 3       8       12           20
                #       6                  16

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_iter(p, key):
    cur = p
    prev = None
    new_node = Node(key)

    while cur is not None:
        prev = cur
        if key < cur.data:
            cur = cur.left
        elif key > cur.data:
            cur = cur.right
        else:
            return

    if key < prev.data:
        prev.left = new_node
    else:
        prev.right = new_node


def insert_rec(p, key):
    if p is None:
        new_node = Node(key)
        return new_node

    if key < p.data:
        p.left = insert_rec(p.left, key)
    elif key > p.data:
        p.right = insert_rec(p.right, key)
    return p


def preorder_rec(p):
    # Time complexity: O(N)
    if p is None:
        return
    print(p.data, end=" ")
    preorder_rec(p.left)
    preorder_rec(p.right)


def inorder_rec(p):
    # Time complexity: O(N)
    if p is None:
        return
    inorder_rec(p.left)
    print(p.data, end=" ")
    inorder_rec(p.right)


def postorder_rec(p):
    # Time complexity: O(N)
    if p is None:
        return
    postorder_rec(p.left)
    postorder_rec(p.right)
    print(p.data, end=" ")


def count_nodes(p):
    if p is None:
        return 0
    return count_nodes(p.left) + count_nodes(p.right) + 1


def level_order(p):
    queue = list()
    queue.insert(0, p)

    while len(queue) != 0:
        cur = queue.pop()
        print(cur.data, end=" ")

        if cur.left is not None:
            queue.insert(0, cur.left)
        if cur.right is not None:
            queue.insert(0, cur.right)


if __name__ == "__main__":
    my_collection = [9, 15, 5, 20, 16, 8, 12, 3, 6]
    root = insert_rec(None, 9)
    for x in my_collection:
        insert_rec(root, x)

    print("Preorder")
    preorder_rec(root)
    print()
    print("Inorder")
    inorder_rec(root)
    print()
    print("Postorder")
    postorder_rec(root)
    print()
    print(count_nodes(root))

    print("Level order")
    level_order(root)