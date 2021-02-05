# https://www.hackerrank.com/challenges/arrays-ds/problem

def reverse_array_sol1(A):
  res_arr = []
  for i in range(len(A)-1, -1, -1):
    res_arr.append(A[i])
  return res_arr

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def reverse_array_sol2(A):
  left = 0
  right = len(A)-1
  
  while left < right:
    swap(A, left, right)
    left += 1
    right -= 1
  return A

# test cases
# [] -> []
# [1] -> [1]
# [1,2] -> [2, 1]
# [1,2, 2, 3] -> [3, 2, 2, 1]

# Solution 1 (time complexity O(N), Space complexity O(N))
# reverse_array = []
# loop i len(arr)-1 to 0
#   reverse_array.append(A[i])
# return reverse_array

# Solution 2 (time complexity O(N), Space complexity O(1))
# swap(arr, i, j):
#   temp = arr[i]
#   arr[i] = arr[j]
#   arr[j] = temp
# 
# left = 0
# right = len(arr) - 1
# while left < right:
#   swap(A, left, right)
#   left += 1
#   right -= 1
# return A

if __name__ == "__main__":
  arr = [1,2, 3]
  res = reverse_array_sol2(arr)
  print(res)