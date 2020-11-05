# // Given 2 arrays, create a function that let's a user know (True/False) whether these two arrays contain any common items
# //For Example:
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# //should return False.
# //-----------
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# //should return True.

# // 2 parameters - arrays - no size limit
# // return True or False

def contains_common_items_slow(arr1, arr2):
    """
    Time Complexity: O(N x M)
    Space Complexity: O(1)
    """
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return True
    return False


def contains_common_items(arr1, arr2):
    """
    Time Complexity: O(N + M)
    Space Complexity: O(N)
    """
    compare_set = set()

    for value in arr1:
        compare_set.add(value)

    for value in arr2:
        if value in compare_set:
            return True
    return False


if __name__ == "__main__":
    array1 = ['a', 'b', 'c', 'x']
    array2 = ['z', 'y', 'i']
    print(contains_common_items_slow(array1, array2))


    array1 = ['a', 'b', 'c', 'x']
    array2 = ['z', 'y', 'x']
    print(contains_common_items(array1, array2))