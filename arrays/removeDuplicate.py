# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


def removeDuplicates(nums):
    """
    Big O(n) -> Time complexity
    Space O(1)
    """
    if nums is None:
        raise TypeError("Nums cannot be None")

    if not isinstance(nums, list):  # ensure the nums specified is alway a list data type
        raise TypeError("Nums can only be a list")

    # if we have 0 or 1 elements in the array
    if len(nums) < 2:
        return len(nums)

    pos = 0 
    for j in range(1, len(nums)):
        if nums[pos] == nums[j]:
            continue
        pos += 1 # increment index
        nums[pos] = nums[j] # update the value at index position

    return pos + 1 # incrementing to get the actual length of unique values


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
