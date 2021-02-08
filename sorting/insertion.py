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
  for i in range(len(arr)-1):
    for j in range(i+1, 0, -1):
      if arr[j-1] > arr[j]:
        swap(arr, j, j-1)
      else:
        break
    
  return arr
 

if __name__ == "__main__":
  arr = [0,4,3,2,1,8]
  print(insertion(arr))