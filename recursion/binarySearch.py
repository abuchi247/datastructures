def binarySearch(container, left, right, item):
  # base case of missed item
  if left > right:
    return -1

  # generate the index of the middle item
  mid = (left + right) // 2

  # we have found the time
  if container[mid] == item:
    return mid

  # check right side of the array
  elif container[mid] < item:
    return binarySearch(container, mid + 1, right, item)
  
  # check items on the left side of the array
  else:
    return binarySearch(container, left, mid-1, item)


if __name__ == "__main__":
  container = [1,2,3,4,5]
  print(binarySearch(container, 0, 5, 5))