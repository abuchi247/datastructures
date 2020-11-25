# Given an array nums of integers, return how many of them contain an even number of digits.

# Constraint
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

# Example 1
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

# Assumptions
# 1. always going to have integers no floating point numbers
# 2. Expect to always have an array passed in
# 3. Elements in the array is always valid
# 4. Numbers are always positive

test1 = '''
def find_numbers_fast(nums):
    even_digit_count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            even_digit_count += 1
    return even_digit_count
'''

test2 = '''
def find_numbers_slow(nums):
    "Big O(N*M)"
    even_digit_count = 0
    def count_digits(num):
        digits = 0
        while num > 0:
            digits += 1
            num = num//10
        return digits
        
    for num in nums:
        if count_digits(num) % 2 == 0:
            even_digit_count += 1
    return even_digit_count

'''

if __name__ == "__main__":
    nums = [12,345,2,6,7896]
    nums = [10 ** 10] * 10

    import timeit
    print(timeit.timeit(stmt = test1, number=1000000))
    print(timeit.timeit(stmt = test2, number=1000000))