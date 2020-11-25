# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
# also in sorted non-decreasing order.


def square(num):
    return num * num


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort_optimized(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                swapped = True
        if not swapped:
            break

def sort_square_with_bubble(array):
    final_array = []

    for num in array:
        final_array.append(square(num))

    bubble_sort_optimized(final_array)
    return final_array


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    final = []

    idx_l = 0
    idx_r = 0

    while idx_l < len(left) and idx_r < len(right):
        if left[idx_l] > right[idx_r]:
            final.append(right[idx_r])
            idx_r += 1
        else:
            final.append(left[idx_l])
            idx_l += 1
    
    if idx_l < len(left):
        final.extend(left[idx_l:])
    else:
        final.extend(right[idx_r:])
    return final

def sort_square_with_merge(array):
    square_array = []

    for num in array:
        square_array.append(square(num))

    square_array = merge_sort(square_array)
    return square_array


if __name__ == "__main__":
    arr = [-7,-4,1, 3, 4, 10]
    print(sort_square_with_merge(arr))
    