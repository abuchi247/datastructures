# Return true or false on whether two strings match or not

def strcmp(str1, str2):
    """
    Compares two strings if they match
    :param str1: first string
    :param str2: second string
    :return: True or false
    """
    if str1 is None or str2 is None:
        print("Raise Error exception")
        return False

    # check they are both strings
    if not isinstance(str1, str):
        print("raise a type error")
        return False

    if not isinstance(str2, str):
        print("raise a type error")
        return False

    # check they length to ensure they are both of the same size
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


def strcmp_rec(str1, str2):
    """
    Compares two strings if they match
    :param str1: first string
    :param str2: second string
    :return: True or false
    """
    if str1 is None or str2 is None:
        print("Raise Error exception")
        return False

    # check they are both strings
    if not isinstance(str1, str):
        print("raise a type error")
        return False

    if not isinstance(str2, str):
        print("raise a type error")
        return False

    # check they length to ensure they are both of the same size
    if len(str1) != len(str2):
        return False

    # base end case
    if len(str1) == 0 and len(str1) == 0:
        return True

    upper_bound = len(str1)-1
    if str1[upper_bound] != str2[upper_bound]:
        return False

    return strcmp_rec(str1[:upper_bound], str2[:upper_bound])


if __name__ == "__main__":
    print("Failure test cases")
    print(strcmp(1, "1") == strcmp_rec(1, "1"))
    print(strcmp("1", 1) == strcmp_rec("1", 1))
    print(strcmp(None, 2) == strcmp_rec(None, 2))
    print(strcmp("123", "12") == strcmp_rec("123", "12"))
    print("Passing test case")
    print(strcmp("12", "12") == strcmp_rec("12", "12"))
    print(strcmp("", "") == strcmp_rec("", ""))