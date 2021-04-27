# Given an array of distinct integers. The task is to count
# all the triplets such that sum of two elements equals the third element.


def triplets(arr):
    if len(arr) < 3:
        return -1

    arr.sort() # sort array first
    arr_set = set(arr)  # get the unique values in the array
    count = 0
    for i in range(len(arr) - 2):
        for j in range(i+1, len(arr)-1):
            s = arr[i] + arr[j]
            if s in arr_set:
                count += 1

    return count if count > 0 else -1


if __name__ == "__main__":
    print(triplets([1, 5, 3, 2]) == 2)
    print(triplets([3, 2, 7]) == -1)
    print(triplets([1, 3, 4, 15, 19]) == 2)
    print(triplets([2, 2, 7, 7, 9]) == 4)
    print(triplets([1, 1, 1, 1, 1, 2]) == 10)
