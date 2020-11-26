# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]
# https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

# Solution 1: N+M


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    final = []

    idx_l = 0
    idx_r = 0

    while idx_l < len(left) and idx_r < len(right):
        if left[idx_l] > right[idx_r]:
            final.append(right[idx_r])
            idx_r += 1
        else:
            final.append(left[idx_l])
            idx_l += 1
    
    if idx_l < len(left):
        final.extend(left[idx_l:])
    else:
        final.extend(right[idx_r:])
    return final

def merge_two(num1, n, num2, m):
  for i in range(m):
    num1[n+i] = num2[i]

  num1 = merge_sort(num1)
  
if __name__ == "__main__":
    num1 = [1, 2, 3, 0,0,0]
    num2 = [2, 2, 2]
    merge_two(num1, 3, num2, 3)
    print(num1)