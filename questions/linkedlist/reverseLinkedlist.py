class Node:

  __slot__ = "data", "next"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next


def print_node(head):
  print("[ ", end="")
  
  while head is not None:
    print(head.data, end=" -> ")
    head = head.next

  print("None ]")

def reverse_node(head):
  prev = None
  cur = head
  while cur is not None:
    next = cur.next
    cur.next = prev
    prev = cur
    cur = next

  head = prev
  return head


if __name__ == "__main__":
  node3 = Node(3)
  node2 = Node(2, node3)
  node1 = Node(1, node2)

  print_node(node1)

  reverse = reverse_node(node1)

  print_node(reverse)