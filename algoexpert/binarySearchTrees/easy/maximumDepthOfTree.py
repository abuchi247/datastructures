# 3. maxDepth()
# Given a binary tree, compute its "maxDepth" -- the number of nodes along the longest path from the root node down
# to the farthest leaf node. The maxDepth of the empty tree is 0, the maxDepth of the tree on the first page is 3.
from buildTree import insert_rec, insert_iter


def getMaxDepth(node):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    if node is None:
        return 0

    x = getMaxDepth(node.left) + 1
    y = getMaxDepth(node.right) + 1
    return max(x, y)


if __name__ == "__main__":
    root = insert_rec(None, 8)
    insert_rec(root, 6)
    insert_iter(root, 14)
    insert_iter(root, 4)
    insert_rec(root, 7)
    insert_rec(root, 16)
    insert_rec(root, 18)
    print(getMaxDepth(root))