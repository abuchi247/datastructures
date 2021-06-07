def strstr(haystack, needle):
    """
    Check for the existence of needle in the haystack
    If it is present as a substring, it should return the position where the needle is present in the haystack
    :param haystack: Original String
    :param needle:  substring to find
    :return: position or a null if not found
    """

    if haystack is None:
        return None
    if needle is None:
        return None

    # Ensure they are both str classes
    if not isinstance(haystack, str):
        # print(f"{haystack} must be a string. Current datatype {type(haystack)}")
        return None

    if not isinstance(needle, str):
        # print(f"{needle} must be a string. Current datatype {type(needle)}")
        return None

    # check if they are empty (I know they are both strings)
    if haystack == "":
        return None

    if needle == "":
        return None

    # check to make sure the haystck is always greater than needle length
    if len(needle) > len(haystack):
        return None

    # Only come here if they needle size is less than the haystack
    size_of_needle = len(needle)

    for i in range(0, len(haystack)):
        end = i + size_of_needle
        # out of bound
        if end > len(haystack):
            return None
        if haystack[i: end] == needle:
            return i
    return None


def strstr_rec(haystack, needle):

    def check_substr(haystack, needle, start):
        if haystack is None:
            return None
        if needle is None:
            return None

        # Ensure they are both str classes
        if not isinstance(haystack, str):
            # print(f"{haystack} must be a string. Current datatype {type(haystack)}")
            return None

        if not isinstance(needle, str):
            # print(f"{needle} must be a string. Current datatype {type(needle)}")
            return None

        # check if they are empty (I know they are both strings)
        if haystack == "":
            return None

        if needle == "":
            return None

        end = len(haystack)

        # check to make sure the haystck is always greater than needle length
        if len(needle) > len(haystack[start:end]):
            return None

        size_of_sub = len(needle)

        if haystack[start: start+size_of_sub] == needle:
            return start
        return check_substr(haystack, needle, start+1)

    return check_substr(haystack, needle, 0)


def solution_3(haystack, needle):
    if haystack is None:
        return None
    if needle is None:
        return None

    # Ensure they are both str classes
    if not isinstance(haystack, str):
        # print(f"{haystack} must be a string. Current datatype {type(haystack)}")
        return None

    if not isinstance(needle, str):
        # print(f"{needle} must be a string. Current datatype {type(needle)}")
        return None

    # check if they are empty (I know they are both strings)
    if haystack == "":
        return None

    if needle == "":
        return None

    # check to make sure the haystck is always greater than needle length
    if len(needle) > len(haystack):
        return None

    # master index for iterating through haystack
    # while loop using the start index (i)
        # get start index for needle (j)
        # temp_i = i
        # found = False
        # while loop j < len(needle) and len(needle[j:]) < len(haystack[temp_i:])
            # if haystack[temp_i] == needle[j]:
                # found needle
                # if j == len(needle):
                    # found = True
                    # break
                # temp_i += 1
                # j += 1
            # else:
                # break
        # if found:
            # return start
    # return None

    start = 0
    while start < len(haystack):
        i = start
        j = 0
        # do this only when j is less than needle length
        # and while remaining contents in needle is less than what remains in haystack
        while j < len(needle) and len(needle[j:]) <= len(haystack[i:]):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                # check if we've found the complete substring
                if j == len(needle):
                    return start
            else:
                break
        start += 1
    return None


if __name__ == "__main__":
    print(strstr("", "") == strstr_rec("", ""))
    print(strstr("2", "") == strstr_rec("2", ""))
    print(strstr("2", "2") == strstr_rec("2", "2"))
    print(strstr("421", "2") == strstr_rec("421", "2"))
    print(strstr("421", 2) == strstr_rec("421", 2))
    print(strstr("!##", "##") == strstr_rec("!##", "##"))
    print(strstr("!##", "###") == strstr_rec("!##", "###"))

    print("Comparing with solution 3")
    print(strstr("", "") == solution_3("", ""))
    print(strstr("2", "") == solution_3("2", ""))
    print(strstr("2", "2") == solution_3("2", "2"))
    print(strstr("421", "2") == solution_3("421", "2"))
    print(strstr("421", 2) == solution_3("421", 2))
    print(strstr("!##", "###") == solution_3("!##", "###"))
