# input: Non empty of distinct numbers array, target sum
# Output: return array of two numbers whose sum is target if present else empty array

# constraints:
# 1.must be two numbers
# 2. Non empty array as input

# Questions
# 1. What happens if the array only has 1 element and the target is the same element? Not valid
# 2. Is the array sorted? No
# 3. Does the order matter when returned? Yes


# Solution 1
# Time complexity O(NxN) Space complexity: O(1)
# for i to len(arr)-1
#    for j starting i+1 until len(arr):
#       if arr[i] + arr[j] == target:
#          return [arr[i], arr[j]]
# return []

# Solution 2:
# Time complexity O(N) Space complexity: O(N)
# lookup = {}
# for i to len(arr):
#    missing_value = target - arr[i]
#    if arr[i] in lookup:
#       return [lookup[missing_value], arr[i]]
#    lookup[missing_value] = arr[i]
# return []


def two_number_sum_sol1(arr, target_sum):
    """
    Time complexity: O(NxN)
    Space complexity: O(1)
    """
    # Write your code here.
    for i in range(len(arr)-1):
        first_num = arr[i]
        for j in range(i + 1, len(arr)):
            second_num = arr[j]
            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []


def two_number_sum_sol2(arr, target_sum):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    nums = set()
    for num in arr:
        potential_match = target_sum - num
        if potential_match in nums:
            return [potential_match, num] # keeping the order of appearance
        nums.add(num)
    return []


def two_number_sum_sol3(arr, target_sum):
    """
    Using a two pointer approach
    Time complexity: O(nlog(n))
    Space complexity: O(1)
    """
    left = 0
    right = len(arr)-1
    arr.sort()

    while left < right:
        sum_value = arr[left] + arr[right]
        # sum is less than target move left point forward
        if sum_value < target_sum:
            left += 1
        elif sum_value > target_sum:
            right -= 1
        else:
            return [arr[left], arr[right]]
    return []


if __name__ == "__main__":
    tests = [
        # cannot be sum of the same number
        {
            "input": {
                "array": [2],
                "target": 2
            },
            "output": []
        },
        # sum not found in array
        {
            "input": {
                "array": [2, 3, 4, 5],
                "target": 10
            },
            "output": []
        },
        # sum found in array
        {
            "input": {
                "array": [2, 3, 4, 5, 6],
                "target": 10
            },
            "output": [4, 6]
        },
        # sum found in array
        {
            "input": {
                "array": [8, 3, 5, 5, 6],
                "target": 10
            },
            "output": [5, 5]
        }
    ]

    for i, test in enumerate(tests):
        result = two_number_sum_sol1(test['input']['array'], test['input']['target'])
        if result != test['output']:
            print(f"test case {i+1} failed: expected {test['output']} but got {result}")

        result = two_number_sum_sol2(test['input']['array'], test['input']['target'])
        if result != test['output']:
            print(f"test case {i + 1} failed: expected {test['output']} but got {result}")

        result = two_number_sum_sol3(test['input']['array'], test['input']['target'])
        if result != test['output']:
            print(f"test case {i + 1} failed: expected {test['output']} but got {result}")