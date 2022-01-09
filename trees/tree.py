from trees.node import Node

class Tree:

    def __init__(self):
        self.root = None

    @classmethod
    def insert_left(cls, root, new_node):
        if root is None:
            root = new_node
        else:
            new_node.set_parent(root)
            root.set_left(new_node)

    @classmethod
    def insert_right(cls, root, new_node):
        if root is None:
            root = new_node
        else:
            new_node.set_parent(root)
            root.set_right(new_node)

    @staticmethod
    def bfs_traversal(root):
        pass


if __name__ == "__main__":
    tree = Tree()
    tree.insert_left(tree.root, Node("A"))
    new_node = Node("B")
    tree.insert_left(tree.root, new_node)
    tree.insert_right(tree.root, Node("C"))
    tree.insert_left(tree.root.get_right(), Node("D"))
    tree.insert_right(tree.root.get_right(), Node("E"))
