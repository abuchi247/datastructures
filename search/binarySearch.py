def find(arr, target):
    if arr is None:
        return False

    if not isinstance(arr, (list, tuple)):
        raise TypeError(f"{arr} is not a list or tuple")

    mid = len(arr) // 2
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
        
        mid = (left + right) // 2
    
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    print(find(arr, 5))