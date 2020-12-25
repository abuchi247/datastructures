# Given n non-negative integers a1, a2, ..., an , where each represents a
#  point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the 
# line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
# such that the container contains the most water.

def get_max_water_container(heights):
    """
    Returns pair of indexs container that holds the most water

    Time complexity: O(N^2)
    Space complexity: O(1)
    """
    max_area = 0

    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            max_area = max(area, max_area)
    return max_area


def get_max_water_container_optimized(heights):
    """
    This solution will be going through the area using two pointer approach and visiting just once.
    The pointer with the smallest value get moved forward.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    max_area = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        area = height * width
        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == "__main__":
    tests = int(input("Number of test cases: "))

    while tests > 0:
        heights = list(map(int, input("Enter an array to get the container with most water: ").split()))

        print(f"Sol 1: Array {heights} container area is {get_max_water_container(heights)}")
        print(f"Sol 2: Array {heights} container area is {get_max_water_container_optimized(heights)}")
        tests -= 1