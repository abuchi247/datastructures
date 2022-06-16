# 4. minValue()
# Given a non-empty binary search tree (an ordered binary tree), return the minimum data value found in that tree.
# Note that it is not necessary to search the entire tree. A maxValue() function is structurally very similar to this
# function. This can be solved with recursion or with a simple while loop
from buildTree import insert_rec, insert_iter


def find_min_value_bfs(node):
    """
    Find the minumum value using BFS traversal
    """
    if node is None:
        return 0

    queue = list()
    queue.append(node)
    minimum = node.data

    while len(queue) > 0:
        cur = queue.pop(0) # pop the first element
        if minimum > cur.data: # update the minimum. We've found a new minimum element
            minimum = cur.data

        # go left
        if cur.left is not None:
            queue.append(cur.left)

        if cur.right is not None:
            queue.append(cur.right)

    return minimum


def find_min_value_preorder_dfs(node, minimum):
    """
    Find the minumum value using pre-order DFS traversal
    """
    if node is None:
        return minimum

    if minimum > node.data:
        minimum = node.data

    minimum = find_min_value_preorder_dfs(node.left, minimum)
    minimum = find_min_value_preorder_dfs(node.right, minimum)

    return minimum


if __name__ == "__main__":
    root = insert_rec(None, 8)
    insert_rec(root, 6)
    insert_iter(root, 14)
    insert_iter(root, 4)
    insert_rec(root, 7)
    insert_rec(root, 16)
    insert_rec(root, 18)
    insert_rec(root, 2)
    insert_rec(root, 20)
    print(find_min_value_bfs(root))
    print(find_min_value_preorder_dfs(root, root.data))