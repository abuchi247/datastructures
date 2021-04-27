# Given an array arr[] of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
#
# Input:
# The first line of input contains T, number of test cases. First line of line each test case contains a single integer N.
# Next line contains N integer array.
#
# Output:
# Print the output of each test case in a seprate line.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 105
# 0 <= a[i] <= 105
#
# Example:
# Input:
# 2
# 7
# 2 6 1 9 4 5 3
# 7
# 1 9 3 10 4 20 2
#
# Output:
# 6
# 4
#
# Explanation:
# Testcase 1:  The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
#
# Testcase2: 1, 2, 3, 4 is the longest consecutive subsequence


def longest_subseq_slow(arr):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    :param arr:
    :return:
    """
    if len(arr) < 1:
        return 0

    # sort arr
    arr.sort()
    max_sum = 1
    for i in range(len(arr)-1):
        local_sum = 1
        for j in range(i, len(arr)):
            if arr[j] + 1 == arr[j+1]:
                local_sum += 1
                max_sum = max(max_sum, local_sum)
            else:
                break
    return max_sum

def longest_subseq(arr):
    """
    Time complexity O(n*log(n))
    Space complexity O(n)
    :param arr:
    :return:
    """
    if len(arr) < 1:
        return 0

    count = 0
    answer = 0
    for i in range(len(arr)-1):
        if arr[i] + 1 == arr[i+1]:
            count += 1
        else:
            count = 1
        answer = max(answer, count)
    return answer

if __name__ == "__main__":
    print(longest_subseq_slow([2, 6, 1, 9, 4, 5, 3]))
    print(longest_subseq_slow([1, 9, 3, 10, 4, 20, 2]))
    print(longest_subseq_slow([1]))
    print(longest_subseq([2, 6, 1, 9, 4, 5, 3]))
    print(longest_subseq([1, 9, 3, 10, 4, 20, 2]))
    print(longest_subseq([1]))
