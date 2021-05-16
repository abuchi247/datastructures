# Find duplicates in a sorted array

def find_duplicates_sol1(arr):
    """
    Time complexity: O(N)
    Space complexity: O(K)
    """
    hash_array = [0]*(max(arr)+1)    # store array of size max element

    # populate the indexs with the occurence in original array
    for i in range(len(arr)):
        index = arr[i]
        hash_array[index] += 1

    count = 0
    for i in range(len(hash_array)):
        if hash_array[i] > 1:
            print(i, end=" ")
            count += hash_array[i]

    return count


def find_duplicates_sol2(arr):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    count = 0
    i = 0

    while i < len(arr) - 1:
        if arr[i] == arr[i+1]:
            j = i
            while arr[j] == arr[i] and j < len(arr):
                j += 1
            count += j - i
            i = j
            print(arr[i-1], end=" ")
        else:
            i += 1
    return count


def find_duplicates_sol3(arr):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    lookup_dict = {}

    for num in arr:
        if num in lookup_dict:
            lookup_dict[num] += 1
        else:
            lookup_dict[num] = 1

    count = 0
    for num in lookup_dict:
        if lookup_dict[num] > 1:
            print(num, end=" ")
            count += lookup_dict[num]

    print(f"Duplicate number count: {count}")


def find_duplicates_sol4(arr):
    """
    Time complexity: O(NxN)
    Space complexity: O(N)
    """
    num_seen = set()
    total_count = 0

    for i in range(len(arr)):
        count = 1
        if arr[i] in num_seen:
            continue
        num_seen.add(arr[i])
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > 1:
            print(arr[i], end=" ")
            total_count += count

    print(f"Duplicate number count: {total_count}")


def find_duplicates_sol5(arr):
    """
    Time complexity: O(NxN)
    Space complexity: O(N)
    """
    total_count = 0

    for i in range(len(arr)):
        count = 1
        if arr[i] is None:
            continue
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                arr[j] = None
                count += 1

        if count > 1:
            print(arr[i], end=" ")
            total_count += count

    print(f"Duplicate number count: {total_count}")


if __name__ == "__main__":
    # arr = [1, 2, 3, 4, 4, 4, 5, 6, 6, 8, 10, 10, 10, 11]
    arr = [8, 3, 6, 4, 6, 5, 6, 8, 2, 7]
    print(find_duplicates_sol1(arr))
    # print(find_duplicates_sol2(arr))
    print(find_duplicates_sol3(arr))
    print(find_duplicates_sol4(arr))
    print(find_duplicates_sol5(arr))