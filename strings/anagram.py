# Find if a string is an anagram or not

def is_anagram_sol1(str1, str2):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    if len(str1) != len(str2):
        return False

    lookup = [0]*128

    for ch in str1:
        pos = ord(ch)
        lookup[pos] += 1

    for ch in str2:
        pos = ord(ch)
        if lookup[pos] == 0:
            return False
        lookup[pos] -= 1

    return True


def is_anagram_sol2(str1, str2):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    if len(str1) != len(str2):
        return False

    lookup = {}

    for ch in str1:
        if ch not in lookup:
            lookup[ch] = 1
        else:
            lookup[ch] += 1

    for ch in str2:
        if ch not in lookup or lookup[ch] == 0:
            return False
        lookup[ch] -= 1

    return True


if __name__ == "__main__":
    str1, str2 = "radar", "aadrr"
    str3, str4 = "aaar", "arra"
    str5, str6 = "aab", "ab"
    print(is_anagram_sol1(str1, str2) == is_anagram_sol2(str1, str2))
    print(is_anagram_sol1(str3, str4) == is_anagram_sol2(str3, str4))
    print(is_anagram_sol1(str5, str6) == is_anagram_sol2(str5, str6))