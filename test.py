tests = [
    {
        "input": [1, 1, 2, 4],
        "output": [1]
    },
    {
        "input": [1, 2, 4],
        "output": []
    },
    {
        "input": [1, 1, 1, 2, 3, 4, 4, 5],
        "output": [1, 4]
    },
    {
        "input": [1],
        "output": []
    },
    {
        "input": [1, 1, 2, 1, 1, 2, 2, 4],
        "output": [1, 2]
    },
]


def find_duplicate_slowest(arr):
    """
    Time complexity: O(NxN)
    Space complexity: O(k)
    """
    duplicate = set()
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                if arr[i] not in duplicate:
                    duplicate.add(arr[i])

    return [x for x in duplicate]


def find_duplicate_sorted(arr):
    """
    Find duplicate elements in a sorted array
    Time complexity: O(N)
    Space complexity: O(k)
    """

    duplicates = []
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            j = i+1
            duplicates.append(arr[i])
            while j < len(arr) and arr[i] == arr[j]:
                j += 1
            i = j
        else:
            i += 1
    return duplicates


def find_duplicate_optimal(arr):
    """
    Finds the duplicate elements in an array
    Time complexity: O(N)
    Space complexity: O(N)
    """

    num_occurrence_dict = {}

    for i in range(len(arr)):
        # checks if it's already in the dictionary
        if arr[i] in num_occurrence_dict:
            num_occurrence_dict[arr[i]] += 1 # increase the occurrence
        else:
            num_occurrence_dict[arr[i]] = 1

    return [x for x in num_occurrence_dict if num_occurrence_dict[x] > 1]


def evaluate_tests(tests, func):
    for test in tests:
        result = func(test["input"])
        if result != test["output"]:
            raise Exception(f"{func.__name__!r} expected {test['output']} but got {result}")
    print(f"{func.__name__!r} test case passed")


if __name__ == "__main__":
    evaluate_tests(tests, find_duplicate_slowest)
    # evaluate_tests(tests, find_duplicate_sorted)
    evaluate_tests(tests, find_duplicate_optimal)
