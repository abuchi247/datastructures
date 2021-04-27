# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.
#
# Output:
# For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= Ai <= 1010
#
# Example:
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5


def sub_array_sum(arr, S, N):
    for i in range(N - 1):
        total = arr[i]
        for j in range(i+1, N):
            if total == S:
                return "{} {}".format(i+1, j)
            elif total > S:
                break
            else:
                total += arr[j]
    return -1


def main():
    T = int(input()) # number or test case
    results = []
    while T > 0:
        N, S = list(map(int, input().strip().split())) # size of array and expected sum
        arr = list(map(int, input().strip().split())) # array element

        results.append(sub_array_sum(arr, S, N))

        T -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    # print(sub_array_sum([1, 2, 3, 7, 5], 12, 5))
    # print(sub_array_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
    arr = sorted([135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134])
    print(sub_array_sum(arr, 468, 42))
    # print(sub_array_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
    # main()