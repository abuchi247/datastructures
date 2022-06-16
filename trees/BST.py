class BinaryTreeNode:

    def __init__(self, data):
        # self.parent = None
        self.left = None
        self.right = None
        self.value = data
        # self.level = -1


class BinarySearchTree:
    """
    A hierarchical dat structure with the following supports

    lookup(value)
    insert(value)
    remove(value)

    """

    def __init__(self):
        self.root = None

    def is_empty(self):
        """
        checks if tree is empty

        Big O(1)
        """
        return self.root is None

    def insert(self, value):
        """
        Inserts a node to a binary search tree

        Constraints:
            1. Only insert to the left node if the value is less than the current node
            2. Only insert to the right node only if the value is greater than current node
            3. Do not insert if the value is equal to the current node

        Big O(N) - if unbalanced and skewed on one direction
        Big O(logN) - if balanced
        """
        # handling Null value
        if value is None:
            raise TypeError("Invalid value type specified")

        # create a node of the value
        new_node = BinaryTreeNode(value)

        # check if the tree is empty
        if self.is_empty():
            # new_node.level += 1 # increment the level 
            self.root = new_node
            return

        # we have at least one node in the tree
        curr = self.root  # walker node
        while curr is not None:
            if curr.value == value:
                print(f"You cannot insert duplicate value: {value}")
                return
            elif value < curr.value:  # go to the left child of node
                if curr.left is None:  # if there's no left child insert it here
                    # new_node.parent = curr
                    # new_node.level = curr.level + 1
                    curr.left = new_node
                    return
                # else there's a left child
                curr = curr.left  # move to the left child
            else:  # check the right  size of the curr node
                if curr.right is None:
                    # new_node.parent = curr  # set the new node parent to be the current node
                    # new_node.level = curr.level + 1
                    curr.right = new_node
                    return
                # else, there's a right child
                curr = curr.right
        return

    def lookup(self, value):
        """
        Searches a binary search tree for a value

        Big O(N) - if unbalanced and skewed on one direction
        Big O(logN) - if balanced
        """
        # check if value is None
        if value is None:
            raise TypeError("Invalid value type specified")

        curr = self.root
        found = False

        while curr is not None and not found:
            if curr.value == value:  # check if value is the current node
                found = True
            # value is less than curr node, move left otherwise move right
            elif curr.value > value:
                curr = curr.left
            else:  # go to the right
                curr = curr.right

        if found:
            # print(f"{curr.value} found on level {curr.level}")
            return curr
        else:
            print(f"{value} is not found")
            return


if __name__ == "__main__":
    BST = BinarySearchTree()
    BST.insert(5)
    BST.insert(7)
    BST.insert(4)
    BST.lookup(4)
