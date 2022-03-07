# Question
# Given an array of integers, return the indices of the two numbers that 
# add up to a given target.

# Constraints
# 1. Assuming the array will always have integers
# 2. Can the array have negative numbers? No
# 3. Can we have duplicate numbers? No
# 4. Will there always be a solution? No
# 5. Can there by multiple pairs summing to the same solution? No

# Test cases:
# []
# [1]
# None
# 2
# [1,2,3,4], target=5
# [1,2,3,4], target=10

# https://leetcode.com/problems/two-sum/

def find_two_sum_brute_force(arr, target):
    """
  Adds all pair of numbers to see if it equals the target

  Time complexity - O(N^2)
  Space complexity - O(1)
  """
    if arr is None:
        return None

    for i in range(len(arr)):
        num_to_find = target - arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] == num_to_find:
                return [i, j]
    return None


def find_two_sum_optimized(arr, target):
    """
  finds the sum of two pairs that equals the target

  """
    if arr is None:
        return None

    nums_map = {}

    for i in range(len(arr)):
        # number to find
        num_to_find = target - arr[i]
        # check if we've seen this number before
        if num_to_find in nums_map:
            return [nums_map[num_to_find], i]

        # add the number to the dictionary along with the index
        nums_map[arr[i]] = i

    # otherwise, return -1, -1 if not found
    return [-1, -1]


if __name__ == "__main__":
    num_test = int(input("Number of test cases: "))

    while num_test > 0:
        arr = list(map(int, input("Enter array separated by space: ").split()))
        target = int(input("Enter a target sum: "))

        print(f"{target} can be achieved by summing {find_two_sum_brute_force(arr, target)}")
        print(f"{target} can be achieved by summing {find_two_sum_optimized(arr, target)}")
        num_test -= 1
