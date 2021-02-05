# Easy -> https://leetcode.com/problems/intersection-of-two-arrays/

# Questions
# Can I assume the array would always container integers? yes
# Can we have more than one intersections? and how would you like me to handle that?
#   Return all the overlapping elements in a unique array
# What happens when we have the same intersection multiple times? 
#   return a single element

# Brute force pseudocode 
#   time complexity = O(NxM), space = O(N)
#   
#   Solution
#   intersections = set()
#   let i loop through N 
#     let j loop through M
#       if N[i] == M[j]:
#         check if we've added that element as an intersection
#         if N[i] in intersections:
#           continue
#         intersections.add(N[j])
#   return list(intersections)

# Optimal pseudocode 
#   time complexity = O(N+M), space = O(N)
#   
#   Solution
#   lookup = set(M)
#   intersections = set()
#   let i loop through N 
#     if i in lookup:
#       if i not in intersections:
#         intersections.add(N[j])
#   return list(intersections)

def intersection_brute_force(nums1, nums2):
  # Time complexity: O(NXM)
  # Space complexity: O(N)
  intersections = set()

  for i in range(len(nums1)):
    for j in range(len(nums2)):
      # check if it's an intersection
      if nums1[i] == nums2[j]:
        if nums1[i] not in intersections:
          intersections.add(nums1[i])
  return list(intersections)


def intersection_optimal(nums1, nums2):
  # Time complexity: O(N+M)
  # Space complexity: O(N)
  intersections = set()
  nums2 = set(nums2)

  for i in range(len(nums1)):
    # check if it's an intersection
    if nums1[i] in nums2:
      if nums1[i] not in intersections:
        intersections.add(nums1[i])
  return list(intersections)


if __name__ == "__main__":
  nums1 = [1,2,2,1]
  nums2 = [2,2]

  print(intersection_brute_force(nums1, nums2) == intersection_optimal(nums1, nums2))

  nums1 = [4,9,5]
  nums2 = [9,4,9,8,4]

  print(intersection_brute_force(nums1, nums2) == intersection_optimal(nums1, nums2))

