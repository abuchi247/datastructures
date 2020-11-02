# This is a demo task.
#
# Write a function:
#
# class Solution { public int solution(int[] A); }
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def find_smallest_positive(A):
    smallest = 1

    for _ in range(len(A)):
        if smallest in set(A):
            smallest += 1
    return smallest


if __name__ == "__main__":
    tests = [
        [1, 3, 6, 4, 1, 2],
        [1, 2, 3],
        [-1, -3],
        [1, 4, 5]
    ]

    for test in tests:
        print(find_smallest_positive(test))