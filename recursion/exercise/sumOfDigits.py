# Calculate the sum of digits in a positive number


tests = [
    {
        "input": 12,
        "output": 3
    },
    {
        "input": 54,
        "output": 9
    },
    {
        "input": 100,
        "output": 1
    },
    {
        "input": 123,
        "output": 6
    },
    {
        "input": 11111,
        "output": 5
    }
]


def sum_of_digits(n):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    assert n >= 0 and n == int(n), "Only support numbers 0 or more and must be an integer!"

    if n < 10:
        return n
    return int(n % 10) + sum_of_digits(n // 10)


if __name__ == "__main__":
    for test in tests:
        result = sum_of_digits(test["input"])
        assert result == test["output"], f"Expected: {test['output']}, got: {result}"
