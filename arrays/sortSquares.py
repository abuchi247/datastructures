# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
# also in sorted non-decreasing order.


def square(num):
    return num * num


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def sort_array(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                swapped = True
        if not swapped:
            break


def sort_square(array):
    final_array = []

    for num in array:
        final_array.append(square(num))

    sort_array(final_array)
    return final_array


if __name__ == "__main__":
    arr = [-7,-4,1, 3, 4, 10]
    print(sort_square(arr))
    