def merge_arrays(a, b):
    """
    Merge two sorted arrays into a single sorted array
    Time complexity: O(N + M)
    Space complexity: O(N + M)
    """
    c = [None] * (len(a) + len(b))

    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1

    # in case we have some elements still in b not in c
    while i < len(a):
        c[k] = a[i]
        k += 1
        i += 1

    # in case we have some elements still in b not in c
    while j < len(b):
        c[k] = b[j]
        k += 1
        j += 1

    return c


if __name__ == "__main__":
    a = [1, 3, 5, 7]
    b = [2, 2, 4, 6]
    print(merge_arrays(a, b))