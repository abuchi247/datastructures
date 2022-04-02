# def move_neg_left(arr):
#     if len(arr) <= 1:
#         return
#     i = 0
#     j = len(arr) - 1
#
#     while i <= j:
#         if arr[i] < 0:
#             i += 1
#             continue
#         if arr[j] >= 0:
#             j -= 1
#             continue
#         swap(arr, i, j)


def move_neg_left(arr):
    if len(arr) <= 1:
        return
    i = 0
    j = 0

    while j < len(arr):
        if arr[j] < 0:
            swap(arr, i, j)
            i += 1
        j += 1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def is_sorted(arr):
    if len(arr) <= 1:
        return True

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False

    return True


if __name__ == "__main__":
    arr = [-6, 3, -8, 10, 5, -7, -9, 12, -4, 2]
    print(arr)
    move_neg_left(arr)
    print(arr)
    print(is_sorted(arr))