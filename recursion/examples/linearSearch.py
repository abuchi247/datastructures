def linear(arr, target, start=0):
  if start >= len(arr):
    return -1

  if arr[start] == target:
    return start

  return linear(arr, target, start+1)


if __name__ == "__main__":
  arr = [1,2,3,4,5]
  print(linear(arr, 5))