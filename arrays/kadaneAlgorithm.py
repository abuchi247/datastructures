# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

# Input:
# The first line of input contains an integer T denoting the number of test cases.
# The description of T test cases follows. The first line of each test case contains a
# single integer N denoting the size of array. The second line contains N space-separated integers
# A1, A2, ..., AN denoting the elements of the array.

# Output:
# Print the maximum sum of the contiguous sub-array in a separate line for each test case.
#
# Constraints:
# 1 ≤ T ≤ 110
# 1 ≤ N ≤ 106
# -107 ≤ A[i] <= 107
#
# Example:
# Input
# 2
# 5
# 1 2 3 -2 5
# 4
# -1 -2 -3 -4
# Output
# 9
# -1

# max_sum = arr[0]
# for i in range(len(arr)-1):
#   total = arr[i]
#   for j in range(i+1, len(arr)):
#       total += arr[j]
#       if total > max_sum:
#           max_sum = total
# return max_sum


def find_max_subarr_sum(arr):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    :param arr:
    :return:
    """
    if len(arr) < 1:
        return 0
    if len(arr) == 1:
        return arr[0]

    max_sum = arr[0]
    for i in range(len(arr)):
        total = arr[i]
        for j in range(i+1, len(arr)):
            total += arr[j]
            # check if we've found a new max sum
            if total > max_sum:
                max_sum = total
    return max_sum

def kadane(arr):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    :param arr:
    :return:
    """
    if len(arr) < 1:
        return 0
    if len(arr) == 1:
        return arr[0]

    local_sum = arr[0]
    global_sum = arr[0]

    for i in range(1, len(arr)):
        local_sum = max(arr[i], local_sum + arr[i])
        global_sum = max(global_sum, local_sum)

    return global_sum

def main() :
    num_testcases = int(input())

    while num_testcases > 0:
        N = int(input())
        arr = list(map(int, input().split()))
        res = find_max_subarr_sum(arr)
        print(res)
        num_testcases -= 1


if __name__ == "__main__":
    # print(find_max_subarr_sum([1, 2, 3, -2, 5]) == 9)
    # print(find_max_subarr_sum([-1, -2, -3, -4]) == -1)
    # print(find_max_subarr_sum([10, 15, 11, 12, 13, -4, -3, -2, -1, 25, 26]))

    main()