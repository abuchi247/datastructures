# Given two strings a and b consisting of lowercase characters.
# The task is to check whether two given strings are anagram of each other or not.
# An anagram of a string is another string that contains same characters, only the order
# of characters can be different. For example, “act” and “tac” are anagram of each other.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# Each test case consist of two strings in 'lowercase' only, in a single line.
#
# Output:
# Print "YES" without quotes if the two strings are anagram else print "NO".
#
# Constraints:
# 1 ≤ T ≤ 300
# 1 ≤ |s| ≤ 106
#
# Example:
# Input:
# 2
# geeksforgeeks forgeeksgeeks
# allergy allergic
#
# Output:
# YES
# NO
#
# Explanation:
# Testcase 1: Both the string have same characters with same frequency. So, both are anagrams.
# Testcase 2: Characters in both the strings are not same, so they are not anagrams.


# def is_anagram(a, b):
#     """
#     Time complexity: O((a+b)log(a+b))
#     Space complexity: O((a+b)log(a+b))
#     """
#     if len(a) != len(b):
#         return "NO"
#
#     a = sorted(a)
#     b = sorted(b)
#
#     if a == b:
#         return "YES"
#     else:
#         return "NO"


def is_anagram(a, b):
    """
    Time complexity: O(a+b)
    Space complexity: O(a+b)
    """
    if len(a) != len(b):
        return "NO"


    a_set = set(a)
    b_set = set(b)

    a_occur_in_b = {}
    b_occur_in_a = {}

    for ch in a:
        if ch in b_set:
            if ch not in a_occur_in_b:
                a_occur_in_b[ch] = 1
            else:
                a_occur_in_b[ch] += 1
        else:
            return "NO"

    for ch in b:
        if ch in a_set:
            if ch not in b_occur_in_a:
                b_occur_in_a[ch] = 1
            else:
                b_occur_in_a[ch] += 1
        else:
            return "NO"

    for key in a_occur_in_b:
        if a_occur_in_b[key] != b_occur_in_a[key]:
            return "NO"
    return "YES"


def count_occurrence(string, ch):
    count = 0
    for i in range(len(string)):
        if string[i] == ch:
            count += 1

    return count


def main():
    T = int(input())
    results = []
    while T > 0:
        a, b = input().strip().split()
        results.append(is_anagram(a, b))
        T -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
