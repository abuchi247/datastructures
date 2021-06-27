# find the duplicates in a string

def found_duplicates_sol1(string):
    """
    Time complexity: O(NxN)
    Space complexity: O(1)
    """
    found = False
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                # print(string[i])
                found = True
    return found


def found_duplicates_sol2(string):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    lookup_array = [0]*128
    found = False

    for ch in string:
        pos = ord(ch)
        if lookup_array[pos] > 0:
            # print(ch)
            found = True
        lookup_array[pos] += 1
    return found


def found_duplicates_sol3(string):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    lookup = {}
    found = False
    for ch in string:
        if ch in lookup:
            # print(ch)
            found = True
            lookup[ch] += 1
        else:
            lookup[ch] = 1
    return found


if __name__ == "__main__":
    t1 = "abachiab"
    t2 = "abuchi"
    t3 = "abi.a"

    print(found_duplicates_sol2(t1) == found_duplicates_sol3(t1))
    print(found_duplicates_sol2(t2) == found_duplicates_sol3(t2))
    print(found_duplicates_sol2(t3) == found_duplicates_sol3(t3))
