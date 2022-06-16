# 2. size()
# http://cslibrary.stanford.edu/110/
# This problem demonstrates simple binary tree traversal. Given a binary tree, count the number of nodes in the tree.
from buildTree import insert_rec, insert_iter


def get_num_of_nodes_preorder(node, accumulator=0):
    """
    Using pre-order DFS traversal to find the number of nodes in a tree - NODE -> LEFT -> RIGHT
    """
    if node is None:
        return accumulator

    accumulator += 1
    # print(f"node: {node.data}, num of nodes: {accumulator}")
    accumulator = get_num_of_nodes_preorder(node.left, accumulator)

    accumulator = get_num_of_nodes_preorder(node.right, accumulator)
    return accumulator


def get_num_of_nodes_inorder(node, accumulator=0):
    """
    Using in-order DFS traversal to find the number of nodes in a tree - LEFT -> NODE -> RIGHT
    """
    if node is None:
        return accumulator

    accumulator = get_num_of_nodes_inorder(node.left, accumulator)
    accumulator += 1
    # print(f"node: {node.data}, num of nodes: {accumulator}")
    accumulator = get_num_of_nodes_inorder(node.right, accumulator)
    return accumulator


def get_num_of_nodes_postorder(node, accumulator=0):
    """
    Using post-order DFS traversal to find the number of nodes in a tree - LEFT -> RIGHT -> NODE
    """
    if node is None:
        return accumulator

    accumulator = get_num_of_nodes_inorder(node.left, accumulator)
    accumulator = get_num_of_nodes_inorder(node.right, accumulator)
    accumulator += 1
    # print(f"node: {node.data}, num of nodes: {accumulator}")
    return accumulator


def get_num_of_nodes(node):
    if node is None:
        return 0
    return get_num_of_nodes(node.left) + get_num_of_nodes(node.right) + 1


if __name__ == "__main__":
    root = insert_rec(None, 8)
    insert_rec(root, 6)
    insert_iter(root, 14)
    insert_iter(root, 4)
    insert_rec(root, 7)
    insert_rec(root, 16)
    print(get_num_of_nodes_preorder(root))
    print(get_num_of_nodes_inorder(root))
    print(get_num_of_nodes_postorder(root))
    print(get_num_of_nodes(root))