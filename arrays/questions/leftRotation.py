# Perform a left rotation by k times

def left_rotate(arr, k):
    k = k % len(arr)

    reverse(0, k-1, arr)
    reverse(k, len(arr)-1, arr)
    reverse(0, len(arr)-1, arr)


def reverse(start, end, arr):
    i = start
    j = end

    while i <= j:
        swap(arr, i, j)
        i += 1
        j -= 1
    return arr


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    left_rotate(arr, 2)

    print(arr)