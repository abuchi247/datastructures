# Given two sorted arrays Arr1[] and Arr2[] in non-decreasing order with size N and M.
# The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).
#
# Note:  DO NOT use extra space. We need to modify existing arrays as following.
#
# Input: Arr1[] = {10};
#        Arr2[] = {2, 3};
# Output: Arr1[] = {2}
#         Arr2[] = {3, 10}
#
# Input: Arr1[] = {1, 5, 9, 10, 15, 20};
#        Arr2[] = {2, 3, 8, 13};
# Output: Arr1[] = {1, 2, 3, 5, 8, 9}
#         Arr2[] = {10, 13, 15, 20}
# Example 1:
#
# Input:
# N = 4, M = 5
# Arr1[] = {1, 3, 5, 7}
# Arr2[] = {0, 2, 6, 8, 9}
# Output: 0 1 2 3 5 6 7 8 9
# Explanation: After merging two non
# decreasing arrays,  we have,
# 0 1 2 3 5 6 7 8 9.
# Example 2:
#
# Input:
# N = 2, M = 3
# Arr1[] = {10, 12}
# Arr2[] = {5, 18, 20}
# Output: 5 10 12 18 20
# Explanation: After merging two non
# decreasing arrays, we have, 5 10 12 18 20.
#
#
# Your Task:
# Complete the function merge() which takes two arrays arr1, arr2 and two integer n, m, as input parameters and returns void. You don't to print answer or take inputs.
#
# Expected Time Complexity: O((n+m)*log(n+m))
# Expected Auxiliary Space: O(1)

# def merge(arr1, arr2, n, m):
#     """
#     Time complexity: O(M+N)
#     Space complexity: O(M+N)
#     :param arr1:
#     :param arr2:
#     :return:
#     """
#     arr1_index = 0
#     arr2_index = 0
#
#     final_arr = []
#
#     while arr1_index < n and arr2_index < m:
#         if arr1[arr1_index] > arr2[arr2_index]:
#             data = arr2[arr2_index]
#             final_arr.append(data)
#             arr2_index += 1
#         else:
#             data = arr1[arr1_index]
#             final_arr.append(data)
#             arr1_index += 1
#
#     # we still have elements in arr1 that needs to be added
#     if arr1_index < n and arr2_index == m:
#         final_arr.extend(arr1[arr1_index:])
#     # still have elements in arr2 that needs to be added
#     if arr1_index == n and arr2_index < m:
#         final_arr.extend(arr2[arr2_index:])
#
#     print(" ".join(str(value) for value in final_arr))


def swap_btw_arrays(arr1, arr2, i, j):
    temp = arr1[i]
    arr1[i] = arr2[j]
    arr2[j] = temp


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# def merge(arr1, arr2, n, m):
#     """
#     Time complexity: O(n * m)
#     Space complexity: O(1)
#     :param arr1:
#     :param arr2:
#     :param n:
#     :param m:
#     :return:
#     """
#     for i in range(n):
#         for j in range(m):
#             if arr1[i] > arr2[j]:
#                 swap_btw_arrays(arr1, arr2, i, j)
#             if j > 0:
#                 if arr2[j-1] > arr2[j]:
#                     swap(arr2, j-1, j)

def merge(arr1, arr2, n, m):
    """
    Time complexity: O(n * m)
    Space complexity: O(1)
    :param arr1:
    :param arr2:
    :param n:
    :param m:
    :return:
    """

    i = 0
    j = 0
    while i < n and j < m:
        if arr1[i] > arr2[j]:
            swap_btw_arrays(arr1, arr2, i, j)
            i += 1
        else:
            i += 1
        arr2.sort()

# [0,2,4]
# [1,3,5]

# iter 1
# [0,1,2]
# [4,3,5]



if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    merge(arr1, arr2, len(arr1), len(arr2))

    for x in arr1:
        print(x, end=" ")

    for x in arr2:
        print(x, end=" ")
    print()

    arr1 = [10, 12]
    arr2 = [5, 18, 20]
    merge(arr1, arr2, len(arr1), len(arr2))

    for x in arr1:
        print(x, end=" ")

    for x in arr2:
        print(x, end=" ")
    print()

    arr1 = [1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 10, 12, 14, 15, 16, 17, 17, 18, 19, 19]
    arr2 = [3]
    merge(arr1, arr2, len(arr1), len(arr2))

    for x in arr1:
        print(x, end=" ")

    for x in arr2:
        print(x, end=" ")
    print()
