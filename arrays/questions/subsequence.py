tests = [
    {
        "input": {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [1, 6, -1, 10]
        },
        "output": True
    },
    {
        "input": {
            "array": [1, 2, 3, 4],
            "sequence": [1, 3, 4]
        },
        "output": True
    },
    {
        "input": {
            "array": [1, 2, 3, 4],
            "sequence": []
        },
        "output": True
    },
]


def isValidSubsequence_sol1(array, sequence):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    seq_idx = 0
    # Write your code here.
    for i in range(len(array)):
        if sequence[seq_idx] == array[i]:
            seq_idx += 1

        if seq_idx == len(sequence):
            return True
    return seq_idx == len(sequence)


def isValidSubsequence_sol2(array, sequence):
    """
    Time complexity: O(N) - N is the longer array
    Space complexity: O(1)
    """
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(sequence)


if __name__ == "__main__":
    for test in tests:
        result = isValidSubsequence_sol1(**test["input"])
        assert result == test["output"], f"Expected: {test['output']} got {result}"