# Compare two string and return
# < 0 if str1 is greater than str2 using the alphabetic order
# = 0  if str1 and str2 are of the same size and have exactly the same case
# > 0 if str2 is greater than str1 using the alphabetic order
def strcmp(str1, str2):
    """

    :param str1:
    :param str2:
    :return:
    """
    if str1 is None and str2 is None:
        return 0

    if str1 is None:
        return 0 - ord(str2[0])

    if str2 is None:
        return ord(str1[0])

    i = 0
    j = 0

    # compare every character
    while i < len(str1) and j < len(str2):
        if ord(str1[i]) != ord(str2[i]):
            return ord(str1[i]) - ord(str2[i])
        i += 1
        j += 1

    if i == len(str1) and j < len(str2):
        return 0 - ord(str2[j])

    if i < len(str1) and j == len(str2):
        return ord(str1[j])

    return 0


if __name__ == "__main__":
    print(strcmp("Abuchi", "abuchi"))
    print(strcmp("AAA", "BCB"))
    print(strcmp("bbb", "aaa"))
