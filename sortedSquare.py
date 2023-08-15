test = [-5, -3, -1, 2, 4, 6]
test = [-1, 2, 4, 6]


def sortedSquaredArraySol1(array):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    # Write your code here.
    final_array = [None] * len(array)
    i = 0
    j = len(array) - 1
    k = j

    while i <= j:
        i_sqr = array[i] ** 2
        j_sqr = array[j] ** 2
        if i_sqr >= j_sqr:
            final_array[k] = i_sqr
            i += 1
        else:
            final_array[k] = j_sqr
            j -= 1
        k -= 1

    print(final_array)
    return final_array


def sortedSquaredArraySol2(array):
    """
    Time complexity: O(NlogN)
    Space complexity: O(N)
    """
    # Write your code here.
    for i in range(len(array)):
        array[i] *= array[i]

    return sorted(array)


