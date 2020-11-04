from time import time

def swap(arr, i, j):
    """
    Swaps elements in arr between the 2 indexes specified
    :param arr:
    :param i:
    :param j:
    :return:
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                swapped = True
                swap(arr, j, j-1)
        if not swapped:
            break


if __name__ == "__main__":
    arr = [i for i in range(10, 0, -1)]

    print("Before sorting")
    # print(arr)
    start = time()
    bubble_sort(arr)
    end = time()
    print("After sorting")
    # print(arr)
    print(f"Sorting duration: {end-start:0.3f} ms")