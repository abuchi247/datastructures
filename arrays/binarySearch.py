def binary_search_iter(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_rec(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_rec(arr, low, mid-1, target)
    else:
        return binary_search_rec(arr, mid+1, high, target)


if __name__ == "__main__":
    arr = [4, 8, 10, 15, 18, 21, 24, 27, 29, 33, 34, 37, 39, 41, 43]
    print(binary_search_rec(arr, 0, len(arr)-1, 4) == binary_search_iter(arr, 4))
    print(binary_search_rec(arr, 0, len(arr)-1, 100) == binary_search_iter(arr, 100))
    print(binary_search_rec(arr, 0, len(arr)-1, -1) == binary_search_iter(arr, -1))
    print(binary_search_rec(arr, 0, len(arr)-1, 18) == binary_search_iter(arr, 18))