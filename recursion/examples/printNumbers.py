def print_head(n):
  # base case
  if n == 0:
    return

  # call recursive function
  print_head(n-1)

  # action
  print(n)


def print_tail(n):
  if n == 0: return 
  print(n)
  print_tail(n-1)

print_head(5)

print_tail(5) 