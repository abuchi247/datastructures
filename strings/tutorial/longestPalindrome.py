# Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
#
# NOTE: Required Time Complexity O(n2).
#
# Input:
# The first line of input consists number of the testcases. The following T lines consist of a string each.
#
# Output:
# In each separate line print the longest palindrome of the string given in the respective test case.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ Str Length ≤ 104
#
# Example:
# Input:
# 1
# aaaabbaa
#
# Output:
# aabbaa
#
# Explanation:
# Testcase 1: The longest palindrome string present in the given string is "aabbaa".


def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start <= end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


def longest_palindrome(string):
    max_len = 0
    max_str = ""

    for i in range(len(string)):
        j = len(string)
        while j > i:
            if is_palindrome(string[i:j]):
                cur_str = string[i:j]
                # print(cur_str)
                palind_len = len(cur_str)
                if max_len < palind_len:
                    max_len = palind_len
                    max_str = cur_str
            j -= 1
    return max_str


def main():
    T = int(input())
    results = []
    while T > 0:
        string = input()
        results.append(longest_palindrome(string))
        T -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
    # print(longest_palindrome("rfkqyuqfjkxy"))
    # print(is_palindrome("rfkqyuqfjkxy"))
