# Your task is to implement the function strstr. The function takes two strings
# as arguments (s,x) and  locates the occurrence of the string x in the string s.
# The function returns and integer denoting the first occurrence of the string x
# in s (0 based indexing).
#
# Example 1:
#
# Input:
# s = GeeksForGeeks, x = Fr
# Output: -1
# Explanation: Fr is not present in the
# string GeeksForGeeks as substring.
# Example 2:
#
# Input:
# s = GeeksForGeeks, x = For
# Output: 5
# Explanation: For is present as substring
# in GeeksForGeeks from index 5 (0 based
# indexing).
# Your Task:
# You don't have to take any input. Just complete the strstr() function which
# takes two strings str, target as an input parameter. The function returns -1 if
# no match if found else it returns an integer denoting the first occurrence of the x
# in the string s.
#
# Expected Time Complexity: O(|s|*|x|)
# Expected Auxiliary Space: O(1)
#
# Note : Try to solve the question in constant space complexity.
#
# Constraints:
# 1 <= |s|,|x| <= 1000


def strstr(haystack, needle):
    # inputs cannot be null
    if haystack is None or needle is None:
        return -1

    # we cannot have other data structures other than strings
    if not isinstance(haystack, str) or not isinstance(needle, str):
        return -1

    # needle cannot be greater than haystack
    if len(needle) > len(haystack):
        return -1

    upper_bound = len(needle)
    index = 0

    while index < len(haystack):
        boundary = index + upper_bound
        if boundary > len(haystack):
            return -1
        
        if haystack[index: boundary] == needle:
            return index
        
        index += 1

def strstr2(haystack, needle):
    # inputs cannot be null
    if haystack is None or needle is None:
        return -1

    # we cannot have other data structures other than strings
    if not isinstance(haystack, str) or not isinstance(needle, str):
        return -1

    # needle cannot be greater than haystack
    if len(needle) > len(haystack):
        return -1

    upper_bound = len(needle)
    index = 0

    while index < len(haystack):
        i = index
        j = 0
        # only if the first two characters matches
        if haystack[i] == needle[j]:
            found = False
            while i < len(haystack) and j < len(needle):
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                    found = True
                else:
                    found = False
                    break
            if found:
                return index

        index += 1
    return -1


if __name__ == "__main__":
    print(strstr2("GeeksForGeeks", "Fr"))
    print(strstr2("GeeksForGeeks", "For"))
    print(strstr2("s", "s"))
