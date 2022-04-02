# Difference of an array are elements in array A < array B

def difference_unsorted(a, b):
    """
    Time complexity: O(NxM)
    Space complexity: O(N+M)
    """
    c = []

    for i in range(len(a)):
        invalid = False
        valid = False
        for j in range(len(b)):
            if a[i] == b[j]:
                invalid = True
                break
            if a[i] < b[j]:
                valid = True

        if valid and not invalid:
            c.append(a[i])

    return c


def difference_sorted(a, b):
    """
    Time complexity: O(N+M)
    Space complexity: O(K) -> K unique elements in N and M
    """
    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            j += 1
            i += 1

    return c


if __name__ == "__main__":
    a = [3, 5, 10, 4, 6]
    b = [12, 4, 7, 2, 5]

    print(difference_unsorted(a, b))

    a = [3, 4, 5, 6, 10]
    b = [2, 4, 5, 7, 12]
    print(difference_sorted(a, b))