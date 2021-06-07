# Given a string s, recursively remove adjacent duplicate characters from the
# string s. The output string should not have any adjacent duplicates.
#
#
# Input:
# The first line of input contains an integer T, denoting the no of test cases.
# Then T test cases follow. Each test case contains a string str.
#
# Output:
# For each test case, print a new line containing the resulting string.
#
# Constraints:
# 1<=T<=100
# 1<=Length of string<=50
#
# Example:
# Input:
# 2
# geeksforgeek
# acaaabbbacdddd
#
# Output:
# gksforgk
# acac


# remove_adjacent_recursive(string):
#     if len(string) <= 1:
#             return string
#       is_duplicate = False
#      function remove_duplicate_recur(string, prev_ch, is_duplicate)
#           if len(string) == 0:
#               return ""
#           if not is_duplicate:
#               if prev_ch != string[0]:
#                   return prev_ch + remove_duplicate_recur(string[1:], string[0], is_duplicate)
#               else:
#                   is_duplicate = True
#                   prev_ch = string[0]
#                   return "" + remove_duplicate_recur(string[1:], string[0], is_duplicate)
#           else:
#               if prev_ch != string[0]:
#                   is_duplicate = False
#                   return "" + remove_duplicate_recur(string[1:], string[0], is_duplicate)
#               else:
#                   return "" + remove_duplicate_recur(string[1:], string[0], is_duplicate)
#       return remove_duplicate_recur(string[1:], string[0], is_duplicate)

# def remove_duplicates(string):
#     if len(string) <= 1:
#         return string
#
#     mid = len(string) // 2
#     left = string[:mid]
#     right = string[mid:]
#
#     remove_duplicates(left)
#     remove_duplicates(right)
#
#     return remove_dup(left, right)
#
# def remove_dup(left, right):
#     c = ""
#     i = 0
#     j = 0
#     duplicate = False
#     while i < len(left) and j < len(right):
#         if left[i] == right[j]:
#


if __name__ == "__main__":
    T = int(input())
    results = []
    while T > 0:
        string = input()
        results.append(remove_duplicates(string))
        T -= 1

    for result in results:
        print(result)