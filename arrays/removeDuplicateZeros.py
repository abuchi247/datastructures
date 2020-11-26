# Given a fixed length array arr of integers, duplicate each occurrence of zero, 
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything from your function.

 

# Example 1:

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]

# https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

def add_zero_move_right(zero_pos, arr):
  if zero_pos > len(arr) - 2:
    return
  
  temp = arr[zero_pos+1:len(arr)-1]

  # insert 0 at zeroth pos+1
  arr[zero_pos+1] = 0

  start = zero_pos + 2

  # copy elements from temp to original array
  for i in range(start, len(arr)):
    arr[i] = temp[i-start]
  return

def remove_duplicate_zeros(arr):
  if len(arr) < 2:
    return
  
  i = 0
  while i < len(arr):
    if arr[i] == 0:
      add_zero_move_right(i, arr)
      i+=2
    else:
      i+= 1

  return


def duplicateZeros(arr) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """

    possible_dups = 0
    length_ = len(arr) - 1

    # Find the number of zeros to be duplicated
    for left in range(length_ + 1):

        # Stop when left points beyond the last element in the original list
        # which would be part of the modified list
        if left > length_ - possible_dups:
            break

        # Count the zeros
        if arr[left] == 0:
            # Edge case: This zero can't be duplicated. We have no more space,
            # as left is pointing to the last element which could be included  
            if left == length_ - possible_dups:
                arr[length_] = 0 # For this zero we just copy it without duplication.
                length_ -= 1
                break
            possible_dups += 1

    # Start backwards from the last element which would be part of new list.
    last = length_ - possible_dups

    # Copy zero twice, and non zero once.
    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + possible_dups] = 0
            possible_dups -= 1
            arr[i + possible_dups] = 0
        else:
            arr[i + possible_dups] = arr[i]


if __name__ == "__main__":
  tests = [
    [1,0,1,2,0],
    [1,1,0,0,1],
    [1,1,1,0,1],
    [1,1,1,1,0],
    [1,2,3,4],
    [0,0,0],
    ]

  for test in tests:
    orig_test = test.copy()
    duplicateZeros(test)
    print(f"{orig_test} -> {test}")