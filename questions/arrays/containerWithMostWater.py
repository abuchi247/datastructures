# Given n non-negative integers a1, a2, ..., an , where each represents a
#  point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the 
# line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
# such that the container contains the most water.

# https://leetcode.com/problems/container-with-most-water/

# Questions:
# 1. Does the width of the lines affect the area calculation? No
# 2. Do the left and right of the graph count as walls? No
# 3. Does a higher line in-between affect the area? No, lines inside a container doesn't affect the area
# [1, 7, 2, 8, 1, 6]

test_cases = [
    # best case
    {
        "input": [7, 1, 2, 3, 9],
        "output": 28
    },
    {
        "input": [7, 8, 2, 10, 3, 6, 9],
        "output": 42
    },
    {
        "input": [7, 9, 2, 10, 3, 8, 11, 9],
        "output": 54
    },
    {
        "input": [],
        "output": 0
    },
    {
        "input": [1],
        "output": 0
    },
]


def find_max_water_container_brute_force(heights):
    """
    Time complexity: O(NxN)
    Space complexity: O(1)
    """
    max_area = 0

    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            width = j - i
            # shorter bar
            length = min(heights[i], heights[j])
            area = length * width
            max_area = max(max_area, area)

    return max_area


def find_max_water_container_optimized(heights):
    """
    #     This solution will be going through the area using two pointer approach and visiting just once.
    #     The pointer with the smallest value get moved forward.
    #
    #     Time complexity: O(N)
    #     Space complexity: O(1)
    #     """
    left = 0
    right = len(heights)-1
    max_area = 0
    while left < right:
        # get the lower height
        height = min(heights[left], heights[right])
        width = right - left
        area = height * width
        max_area = max(area, max_area)

        # move only the lower pointer
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


def evaluate_tests(func, tests):
    print(f"Executing {func.__name__!r}")
    for test in tests:
        result = func(test["input"])
        if test["output"] == result:
            print(f"PASSED: {test['input']}")
        else:
            raise Exception(f"FAILED: {test['input']}. Expected {test['output']} got {result}")


if __name__ == "__main__":
    # tests = int(input("Number of test cases: "))
    #
    # while tests > 0:
    #     heights = list(map(int, input("Enter an array to get the container with most water: ").split()))
    #
    #     print(f"Sol 1: Array {heights} container area is {get_max_water_container(heights)}")
    #     print(f"Sol 2: Array {heights} container area is {get_max_water_container_optimized(heights)}")
    #     tests -= 1
    evaluate_tests(find_max_water_container_brute_force, test_cases)
    evaluate_tests(find_max_water_container_optimized, test_cases)
