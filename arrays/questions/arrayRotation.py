def shift_left_rotate(arr, shifts):
    """
    Time complexity: O(N x shifts)
    Space complexity: O(1)
    """
    if len(arr) <= 1:
        return

    for _ in range(shifts):
        shift_left(arr)


def shift_left(arr):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr) - 1] = temp


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    shift_left_rotate(arr, 7)
    print(arr)

