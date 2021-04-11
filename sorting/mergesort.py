def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    left_idx = 0
    right_idx = 0
    final_arr = []
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            final_arr.append(left[left_idx])
            left_idx += 1
        else:
            final_arr.append(right[right_idx])
            right_idx += 1
    
    if left_idx < len(left):
        final_arr.extend(left[left_idx:])
    
    if right_idx < len(right):
        final_arr.extend(right[right_idx:])
        
    return final_arr

if __name__ == "__main__":
  # arr = [0,4,3,2,1,8]
  # print(insertion(arr))
  arr = [i for i in range(1000000, 0, -1)]
  from time import time
  print("Before sorting")
  # print(arr)
  start = time()
  merge_sort(arr)
  end = time()
  print("After sorting")
  # print(arr)
  print(f"Sorting duration: {end-start:0.3f} ms")