class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def add_children(self, left, right):
    self.left = left
    self.right = right


def sameTree(head1, head2):
  """
  Time complexity: O(N)
  """
  # if both nodes are Null return true
  if head1 is None and head2 is None:
    return True

  if head1 is None:
    return False

  elif head2 is None:
    return False

  # check if the root at the left and right are the same for both nodes
  if sameTree(head1.left, head2.left) and sameTree(head1.right, head2.right):
    return head1.value == head2.value # check the values of the current nodes

  return False
  