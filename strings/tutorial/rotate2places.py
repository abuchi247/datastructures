# Given two strings a and b. The task is to find if a string 'a' can be obtained by
# rotating another string 'b' by 2 places.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases.
# Then T test cases follow. In the next two line are two string a and b.
#
# Output:
# For each test case in a new line print 1 if the string 'a' can be obtained by
# rotating string 'b' by two places else print 0.
#
# Constraints:
# 1 <= T <= 50
# 1 <= length of a, b < 100
#
# Example:
# Input:
# 2
# amazon
# azonam
# geeksforgeeks
# geeksgeeksfor


def rotate2places(a, b):
    """
    Time complexity: 2
    Space complexity: N
    :param a:
    :param b:
    :return:
    """
    if len(a) != len(b):
        return 0

    for i in range(2):
        a = a[1:] + a[0]

    return 1 if a == b else 0

if __name__ == "__main__":
    a = "amazon"
    b = "azonam"
    print(rotate2places(a, b))
    a = "geeksforgeeks"
    b = "geeksgeeksfor"
    print(rotate2places(a, b))
