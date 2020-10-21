# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


def remove_duplicate(nums):
    if len(nums) == 0: return 0
    index = 0
    while index < len(nums) - 1:
        if nums[index] == nums[index + 1]:
            nums.pop(index+1) # remove that element
        else:
            index += 1
    return len(nums)


def remove_duplicate(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    size = remove_duplicate(nums)
    print(size)
    for i in range(size):
        print(nums[i], end=",")
    print()
    nums = [0,0,1,1,1,2,2,3,3,4]
    size = remove_duplicate(nums)
    print(size)
    for i in range(size):
        print(nums[i], end=",")
