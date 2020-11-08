# Find the first recurring num in an array else return None

# Given an array = [2,5,1,2,3,4,1] => 2
# Given an array = [1, 0, 0, 1] => 0
# Given an array = [1, 2, 0, 3] => None


def find_first_recur_num_slow(nums):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return None


def find_first_recur_num(nums):
    nums_seen = set()

    for num in nums:
        if num in nums_seen:
            return num
        nums_seen.add(num)

    return None


if __name__ == "__main__":
    nums = [1, 2, 0, 3]
    nums = [1, 0, 0, 1]
    print(find_first_recur_num_slow(nums))