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

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j) # swap elements

if __name__ == "__main__":
    arr = [5,4,3,2,8]

    selection_sort(arr)

    print(arr)