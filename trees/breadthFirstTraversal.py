def breadthFirst(node):
    """
    Uses the breadth first traversal algorithm to traverse a binary tree. it uses a queue to ensure its visiting the
    correct nodes
    """

    queue = list()  # using a list for now with the assuming of with an actual queue we will get O(1) for dequeue and enqueue
    queue.append(node) # add the root node to the queue

    while len(queue) > 0: # do this until the queue is empty
        curr = queue.pop(0) # remove the first element from the queue
        print(curr.get_data()) # print the data of the current node

        # visit the left node if it exists and add to the queue
        if curr.get_left_child() is not None:
            queue.append(curr.get_left_child())

        # visit the right node if it exists and add to the queue
        if curr.get_right_child() is not None:
            queue.append(curr.get_right_child())