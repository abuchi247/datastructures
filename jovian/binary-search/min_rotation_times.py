# You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
# Your function should have the worst-case complexity of O(log N), where N is the length of the list.
# You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
#
# We define "rotating a list" as removing the last element of the list and adding it before the first element.
# E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
#
# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

# Test cases
# No number in the list
# Single number in the list
# Sorted number without any rotation
# List with 2 numbers but 1 rotation
# List of 5 elements with 2 rotations
# List of 5 elements with 4 rotations
# List of 4 elements with 2 rotations
# List of 4 elements with 3 rotations
# List of 5 elements with 5 rotations
# List with repeating elements rotated 3 times
# List with repeating elements with repeating value at the beginning and end

tests = [
    {
        "input": {
            "nums": []
        },
        "output": 0
    },
    {
        "input": {
            "nums": [1]
        },
        "output": 0
    },
    {
        "input": {
            "nums": [1, 2, 3, 4, 5]
        },
        "output": 0
    },
    {
        "input": {
            "nums": [2, 1]
        },
        "output": 1
    },
    {
        "input": {
            "nums": [4, 5, 1, 2, 3]
        },
        "output": 2
    },
    {
        "input": {
            "nums": [2, 3, 4, 5, 1]
        },
        "output": 4
    },
    {
        "input": {
            "nums": [4, 5, 2, 3]
        },
        "output": 2
    },
    {
        "input": {
            "nums": [3, 4, 5, 2]
        },
        "output": 3
    },
    {
        "input": {
            "nums": [1, 2, 3, 4, 5]
        },
        "output": 0
    },
    {
        "input": {
            "nums": [7, 8, 1, 2, 3, 4, 5, 6]
        },
        "output": 2
    },
    {
        "input": {
            "nums": [1, 2, 3, 4, 5, -1, 0]
        },
        "output": 5
    },
    {
        "input": {
            "nums": [2, 2, 2, 3, 4, 1, 2]
        },
        "output": 5
    },
    {
        "input": {
            "nums": [2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 1, 2]
        },
        "output": 10
    }
]

# Go through every element until we find a position where position is less than the number before it
# otherwise, repeat until we've exhausted our search
# return 0
def count_rotation_linear(nums):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position
        position += 1
    return 0

# Set low index to 0
# high index to len(array) - 1
# mid index = low + high // 2
# if mid > 0 and number at the mid < number at mid - 1 then return mid
# elif number at low is less than or equal to number at mid and number at mid greater than number at high
# set low to mid + 1
# else: set high to mid - 1
# repeat step 3 to the end until we've exhausted our search space
# return 0
def count_rotation_binary(nums):
    if len(nums) <= 1: return 0
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # locate the position where the value besides the mid is greater than the mid
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid

        # search right
        elif nums[low] <= nums[mid] and nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    return low


if __name__ == "__main__":
    for index, test in enumerate(tests):
        result = count_rotation_linear(**test['input'])
        if result != test['output']:
            print("result", result)
            raise Exception(f"Test {index}: failed, input: {test['input']}")
