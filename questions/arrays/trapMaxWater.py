# Given n non-negative integers representing an elevation map where the width of 
# each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# Explanation: The above elevation map (black section) is represented by array 
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are 
# being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Example 3:
# [3, 4, 3] => 0
# [3, 2, 1, 2, 4] => 4
# [4, 0, 3, 2, 0, 5] => 11

# https://leetcode.com/problems/trapping-rain-water/

def trap_brute_force(height):
  """
  Time complexity: N*N
  Space complexity: 1
  """
  total_water = 0

  for index in range(len(height)):
    left_index = index
    right_index = index
    max_left = 0
    max_right = 0

    # find the maximum height to the left of the current height
    while left_index >= 0:
      max_left = max(max_left, height[left_index]) # get the maximum height to the left of cur_height
      left_index -= 1
    
    # find the maximum height to the right of the current height
    while right_index < len(height):
      max_right = max(max_right, height[right_index]) # get the maximum height to the right of cur_height
      right_index += 1

    cur_water = min(max_left, max_right) - height[index]

    if cur_water >= 0:
      total_water += cur_water

  return total_water


def trap_optimized(height):
  """
  Time complexity: O(N)
  Space complexity: O(1)
  """
  total_rain = 0
  max_left = 0
  max_right = 0
  left = 0
  right = len(height) - 1
  
  
  while left < right:
      if height[left] <= height[right]:
          if height[left] >= max_left:
              max_left = height[left]
          else:
              total_rain = max_left - height[left]
          left += 1

      else:
          if height[right] >= max_right:
              max_right = height[right]
          else:
              total_rain = max_right - height[right]
          right -= 1
          
  return total_rain


if __name__ == "__main__":
  num_test = int(input("Number of test cases: "))

  while num_test > 0:
    height = list(map(int, input("Enter heights: ").split(",")))

    print(f"{height} can hold {trap_brute_force(height)} water")
    print(f"{height} can hold {trap_optimized(height)} water")
    num_test -= 1