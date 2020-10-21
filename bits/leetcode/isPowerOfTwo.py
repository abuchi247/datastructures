# Given an integer n, write a function to determine if it is a power of two.
#
# Example 1:
#
# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:
#
# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:
#
# Input: n = 3
# Output: false
# Example 4:
#
# Input: n = 4
# Output: true
# Example 5:
#
# Input: n = 5
# Output: false

def isPowerOfTwo(n):
    """
    Returns truw or false if the number is a power of 2
    :param n:
    :return:
    """
    count = 0
    while n > 0:
        count += 1
        n = n & (n - 1)
    return True if count == 1 else False

def isPowerOfTwoSol2(n):
    if n <= 0:
        return False
    if n & (n - 1) == 0:
        return True
    return False


if __name__ == "__main__":
    T = int(input("Enter number of test cases: "))

    while T > 0:
        N = int(input("Enter a number to check if it's a power of 2: "))
        print(f"Solution 1: {isPowerOfTwo(N)}")
        print(f"Solution 2: {isPowerOfTwoSol2(N)}")
        T -= 1
