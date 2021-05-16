# Find the pair of number which sums up to a particular target sum

def find_pair_sol1(arr, target):
    """
    Time complexity: NxN
    Space complexity: 1
    """
    results = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                print([arr[i], arr[j]])


def find_pair_sol2(arr, target):
    """
    Time complexity: N
    Space complexity: N
    """
    if len(arr) == 0:
        return

    max_value = max(arr)
    lookup_hash = [0] * (max_value + 1)

    for i in range(len(arr)):
        diff = target - arr[i]
        if diff < 0 or diff > len(lookup_hash)-1:
            continue
        # check the index if it's seen before
        if lookup_hash[diff] == 1:
            print([diff, arr[i]])

        lookup_hash[arr[i]] = 1

def find_pair_sol3(arr, target):
    """
    Optimal solution for sorted array
    Time complexity: N
    Space complexity: 1
    """
    i = 0
    j = len(arr) - 1

    while i < j:
        total = arr[i] + arr[j]
        if total == target:
            print([arr[i], arr[j]])
            i += 1
            j -= 1
        elif total < target:
            i += 1
        else:
            j -= 1


if __name__ == "__main__":
    print('Slow solution')
    arr = [[], 10]
    find_pair_sol1(arr[0], arr[1])
    arr = [[1, 2, 3, 4], 5]
    find_pair_sol1(arr[0], arr[1])
    arr = [[1, 2, 3, 4], 10]
    find_pair_sol1(arr[0], arr[1])

    print('Faster solution')
    arr = [[], 10]
    find_pair_sol2(arr[0], arr[1])
    arr = [[1, 2, 3, 4], 5]
    find_pair_sol2(arr[0], arr[1])
    arr = [[1, 2, 3, 4], 10]
    find_pair_sol2(arr[0], arr[1])

    print('Faster Sorted Array Solution')
    arr = [[], 10]
    find_pair_sol3(arr[0], arr[1])
    arr = [[1, 2, 3, 4], 5]
    find_pair_sol3(arr[0], arr[1])
    arr = [[1, 2, 3, 4], 10]
    find_pair_sol3(arr[0], arr[1])