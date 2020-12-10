def find(arr, target):
    """
    Big O(N)
    """
    if arr is None:
        return False
        
    if not isinstance(arr, (list, tuple)):
        raise TypeError(f"{arr} is not a list or tuple")

    for i in range(len(arr)):
        if target == arr[i]:
            return True
    
    return False


if __name__ == "__main__":
    arr = [12, 5]

    print(find(arr, 5))