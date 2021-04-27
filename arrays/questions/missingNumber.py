# Given an array C of size N-1 and given that there are numbers
# from 1 to N with one element missing, the missing number is to be found.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# For each test case first line contains N(size of array). The subsequent line
# contains N-1 array elements.
#
# Output:
# Print the missing number in array.
#
# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 107
# 1 ≤ C[i] ≤ 107
#
# Example:
# Input:
# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10
#
# Output:
# 4
# 9
#
# Explanation:
# Testcase 1: Given array : 1 2 3 5. Missing element is 4.


# def find_missing_number(arr, N):
#     """
#     Time complexity: O(N)
#     Space complexity: O(N)
#     :param arr:
#     :param N:
#     :return:
#     """
#
#     arr_set = set(arr)
#     for i in range(1, N+1):
#         if i not in arr_set:
#             return i
#     return -1


def find_missing_number(arr, N):
    """
    Time complexity: O(NLog(N))
    Space complexity: O(1)
    :param arr:
    :param N:
    :return:
    """
    arr.sort()
    if arr[0] != 1:
        return 1

    if arr[-1] != N:
        return N

    for i in range(len(arr)):
        if arr[i]+1 != arr[i+1]:
            return arr[i]+1
    return -1


def main():
    T = int(input())
    results = []
    while T > 0:
        N = int(input())
        arr = list(map(int, input().strip().split()))
        results.append(find_missing_number(arr, N))
        T -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
