# Find the maximum and minimum number of an array in a single scan

def find_max_min(arr):
    if len(arr) == 0:
        return

    max_num = min_num = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
        elif arr[i] < min_num:
            min_num = arr[i]

    print("Max: ", max_num)
    print("Min: ", min_num)


if __name__ == "__main__":
    arr = [3, 2, -1, 3, 5, 2, 10, -1]
    find_max_min(arr)