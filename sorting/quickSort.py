from time import time

def quick_sort(arr, left, right):
  if left >= right: return

  mid = (left + right) // 2
  pivot = arr[mid]
  index = partition(arr, left, right, pivot)
  quick_sort(arr, left, index-1)
  quick_sort(arr, index, right)


def partition(arr, left, right, pivot):
  while left <= right:
    while arr[left] < pivot:
      left += 1

    while arr[right] > pivot:
      right -= 1

    if left <= right:
      swap(arr, left, right)
      left += 1
      right -= 1

  return left

def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
  # arr = [10, 7, 8, 9, 1, 5] 
  # # arr = [0,4,3,2,1,8]
  # arr = [0,0,0]
  # n = len(arr) 
  # quick_sort(arr, 0, n-1) 
  # print(arr)
  arr = [i for i in range(1000000, 0, -1)]

  print("Before sorting")
  # print(arr)
  start = time()
  quick_sort(arr, 0, len(arr)-1)
  end = time()
  print("After sorting")
  # print(arr)
  print(f"Sorting duration: {end-start:0.3f} ms")