def preorder(root):
    """
    Uses the preorder traversal approach to visit the nodes in a preorder manner: NODE -> LEFT SUBTREE -> RIGHT SUBTREE
    """
    if root is None:
        return

    print(root.get_data())  # process the node
    preorder(root.get_left_child())  # go to the left child
    preorder(root.get_right_child())  # go to the right child


def inorder(root):
    """
    Uses the inorder traversal approach to visit the nodes in a inorder manner: LEFT SUBTREE -> NODE -> RIGHT SUBTREE
    """
    if root is None:
        return

    preorder(root.get_left_child())  # go to the left child
    print(root.get_data())  # process the node
    preorder(root.get_right_child())  # go to the right child


def postorder(root):
    """
    Uses the postorder traversal approach to visit the nodes in a postorder manner:
    LEFT SUBTREE -> RIGHT SUBTREE -> NODE
    """
    if root is None:
        return

    preorder(root.get_left_child())  # go to the left child
    preorder(root.get_right_child())  # go to the right child
    print(root.get_data())  # process the node
