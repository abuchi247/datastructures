def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def insertion_sol1(arr):
  if len(arr) < 2:
    return arr
  
  for index in range(1, len(arr)):
    i = index-1
    j = index

    while i >= 0:
      if arr[i] > arr[j]:
        swap(arr, i, j)
      else:
        break
      i -= 1
      j -= 1

  return arr

def insertion(arr):
  # go up to the second to the last element
  for i in range(len(arr)-1): 
    # bubble the elements outside of the sorted sub-array to the right position
    for j in range(i+1, 0, -1): 
      if arr[j-1] > arr[j]:
        swap(arr, j, j-1)
      else:
        # if the element is in the right position in the sorted array then there's no sort needed
        break
    
  return arr
 

if __name__ == "__main__":
  # arr = [0,4,3,2,1,8]
  # print(insertion(arr))
  arr = [i for i in range(100000, 0, -1)]
  from time import time
  print("Before sorting")
  # print(arr)
  start = time()
  insertion(arr)
  end = time()
  print("After sorting")
  # print(arr)
  print(f"Sorting duration: {end-start:0.3f} ms")