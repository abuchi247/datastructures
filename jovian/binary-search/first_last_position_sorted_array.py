# Question: Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given number.


def binary_search(lo, hi, condition):

    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def first_position(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid - 1 >= 0 and nums[mid - 1] == target:
                return "left"
            else:
                return "found"
        elif nums[mid] > target:
            return "left"
        else:
            return "right"

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid + 1 < len(nums) and nums[mid + 1] == target:
                return "right"
            else:
                return "found"
        elif nums[mid] > target:
            return "left"
        else:
            return "right"

    return binary_search(0, len(nums) - 1, condition)


def find_first_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


if __name__ == "__main__":
    nums = []
    print(find_first_last_position(nums, 1))