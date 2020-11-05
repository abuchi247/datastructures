# [1, 2, 3, 9]   Sum = 8 
# [1, 2, 4, 4]   Sum = 8

# def has_pair_with_sum(arr, sum):
#     if arr is None:
#         return False

#     low = 0
#     high = len(arr) - 1
#     found = False

#     while low < high and not found:
#         pair_sum = arr[low] + arr[high]
#         if pair_sum == sum:
#             found = True
#         elif pair_sum > sum:
#             high -= 1
#         else:
#             low += 1

#     return (found, (-1, -1)) if not found else (found, (low, high))


def has_pair_with_sum(arr, sum):
    if arr is None:
        return False

    complements = set()

    for value in arr:
        if value in complements:
            return True
        complements.add(sum - value)

    return False


if __name__ == "__main__":
    arr =  [1, 2, 3, 9] 
    arr =  [1, 2, 4, 4] 
    arr =  [-2, -1, 0, 7, 8] 

    print(has_pair_with_sum(arr, 8))