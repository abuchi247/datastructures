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


def find_missing_number_sorted_sol1(arr):
    """
    Time complexity: O(N x k) -> k = number of missing elements
    Space complexity: O(k) -> number of missing elements
    :param arr:
    :param N:
    :return:
    """
    missing_nums = []
    if len(arr) > 1:
        for i in range(len(arr)-1):
            desired_next = arr[i] + 1
            while desired_next != arr[i + 1]:
                missing_nums.append(desired_next)
                desired_next += 1
    return missing_nums


def find_missing_number_sorted_sol2(arr):
    """
    Finds only one missing element using the index to compute the missing element
    Time complexity: O(N x k) -> k = number of missing elements
    Space complexity: O(k) -> number of missing elements
    :param arr:
    :param N:
    :return:
    """
    low = arr[0]
    diff = low - 0
    missing_num = []

    for i in range(len(arr)):
        # ensure the difference between the number and the index are always the same the first element
        if (arr[i] - i) != diff:
            # keep storing the values missing until the current difference is equal to the new difference
            while diff < arr[i] - i:
                missing_num.append(i + diff)
                diff += 1
    return missing_num


def find_missing_number_sorted_sol3(arr):
    """
    Finds only one missing element
    Time complexity: O(N)
    Space complexity: O(1)
    :param arr:
    :param N:
    :return:
    """
    soe = sum(arr)
    high = arr[-1]
    s = high * (high + 1) // 2
    return s - soe


def find_missing_number_optimal(arr):
    """
    Time complexity: O(N)
    Space complexity: O(k)
    """
    min_element = min(arr)
    max_element = max(arr)
    # creating a hash table
    miss_array = [0]*(max_element+1)

    # populating the hashtable
    for i in range(len(arr)):
        value = arr[i]
        # constant time
        miss_array[value] += 1

    # iterating over the hashtable
    for i in range(min_element, len(miss_array)):
        # display only the elements missing == 0 value
        if miss_array[i] == 0:
            print(i, end=" ")


def sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total


if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 9, 14, 20]
    # print(find_missing_number_sorted_sol1(arr))
    print(find_missing_number_sorted_sol2(arr))
    # print(find_missing_number_sorted_sol3(arr))
    find_missing_number_optimal(arr)
