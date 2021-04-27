def shift_left_rotate(arr, shifts):
    if len(arr) <= 1:
        return

    for _ in range(shifts):
        shift_left(arr)


def shift_left(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr) - 1] = temp


