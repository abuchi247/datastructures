# Given a binary array, find the maximum number of consecutive 1s in this array.
# [0,1,0,1,0,1,1,0,1] -> 2
# [0, 1, 0] -> 1
# [1,1,1,1] -> 4
# [0,0,0] -> 0

def count_consecutive_1s_slow(arr):
    """ 
    Time complexity = O(N^2)
    Space complexity = O(1)
    """
    max_ones = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        count = 1
        for j in range(i+1, len(arr)):
            if arr[j] == 1:
                count += 1
            else:
                break
        max_ones = max(count, max_ones)

    return max_ones


def count_consecutive_1s(arr):
    """ 
    Time complexity = O(n)
    Space complexity = O(1)
    """
    max_ones = 0
    count = 0
    for num in arr:
        if num:
            count += 1
        else:
            count = 0
        max_ones = max(count, max_ones)
    return max_ones


if __name__ == "__main__":
    arrs = [
        [0,1,0,1,0,1,1,0,1],
        [0, 1, 0],
        [1,1,1,1],
        [0,0,0]
        ]

    for arr in arrs:
        print(count_consecutive_1s(arr))
        print(count_consecutive_1s_slow(arr))