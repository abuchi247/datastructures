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


def selection_sort(arr):
    """
    Using the selection sort to sort the array
    :param arr:
    :return:
    """

    for i in range(len(arr)):    # for each iteration, we put the smallest element in the right position
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j) # swap elements

if __name__ == "__main__":
    arr = [i for i in range(10, 0, -1)]

    print("Before sorting")
    # print(arr)
    start = time()
    selection_sort(arr)
    end = time()
    print("After sorting")
    # print(arr)
    print(f"Sorting duration: {end-start:0.3f} ms")