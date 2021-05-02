# Union of an array is a list of all elements in both array without duplicating any element

def union_unsorted(a, b):
    """
    Time complexity: O(NxM)
    Space complexity: O(N+M)
    """
    c = []

    for num in a:
        c.append(num)

    for num in b:
        found = False
        for value in c:
            if num == value:
                found = True
                break
        if not found:
            c.append(num)

    return c


def union_sorted(a, b):
    """
    Time complexity: O(N+M)
    Space complexity: O(N+M)
    """
    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif b[j] < a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


if __name__ == "__main__":
    a = [3, 5, 10, 4, 6]
    b = [12, 4, 7, 2, 5]

    print(union_unsorted(a, b))

    a = [3, 4, 5, 6, 10]
    b = [2, 4, 5, 7, 12]
    print(union_sorted(a, b))