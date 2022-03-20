from time import time


tests = [
    {
        "input": [5, 4, 3, 2, 1],
        "output": [1, 2, 3, 4, 5]
    },
    {
        "input": [1],
        "output": [1]
    },
    {
        "input": [5, 1, 2, 3, 4],
        "output": [1, 2, 3, 4, 5]
    },
    {
        "input": [],
        "output": []
    },
    {
        "input": [1, 3, 3, 2, 2, 1],
        "output": [1, 1, 2, 2, 3, 3]
    },
    {
        "input": [4, 2, 1, 7, 8, 3],
        "output": [1, 2, 3, 4, 7, 8]
    },
    {
        "input": [i for i in range(100000, 0, -1)],
        "output": [i for i in range(0, 100001)]
    }
]


def swap(arr, i, j):
    """
    Time complexity: O(1)
    Space complexity: O(1)
    """
    arr[i], arr[j] = arr[j], arr[i]


def insertion_v1(arr):
    """
    Time complexity: O(N)
    Space complexity: O(k)
    """
    for i in range(1, len(arr)):
        j = i
        # bubble the elements outside of the sorted sub-array to the right position or no need
        # to bubble if it's alraedy in the right place
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1
    return arr


def insertion_v2(arr):
    # go up to the second to the last element
    for i in range(len(arr) - 1):
        # bubble the elements outside of the sorted sub-array to the right position
        for j in range(i + 1, 0, -1):
            if arr[j - 1] > arr[j]:
                swap(arr, j, j - 1)
            else:
                # if the element is in the right position in the sorted array then there's no sort needed
                break
    return arr


def insertion_v3(arr):
    if len(arr) < 2:
        return arr

    for index in range(1, len(arr)):
        i = index - 1
        j = index

        while i >= 0:
            if arr[i] > arr[j]:
                swap(arr, i, j)
            else:
                break
            i -= 1
            j -= 1

    return arr


def evaluate_tests(tests, func):
    for i, test in enumerate(tests):
        start = time()
        result = func(test["input"])
        end = time()
        if result != test["output"]:
            raise Exception(f"{func.__name__!r} expected {test['output']} but got {result}")
        else:
            print(f"{func.__name__!r} test case: {i+1} elapsed time: {end-start:0.3f} ms")
    print(f"{func.__name__!r} test case passed")


if __name__ == "__main__":
    evaluate_tests(tests, insertion_v1)
    evaluate_tests(tests, insertion_v2)
    evaluate_tests(tests, insertion_v3)
