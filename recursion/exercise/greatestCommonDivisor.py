# How to find the GCD (Greatest Common Divisor) of two numbers using recursion?
# gcd(8, 12) = 4
# 8 = 2 * 2 * 2
# 12 = 2 * 2 * 3

# Euclidean algorithm
# gcd(48,18)
# Step 1: 48/18 = 2 remainder 12
# Step 2: 18/12 = 1 remainder 6
# Step 3: 12/6 = 2 remainder 0


tests = [
    {
        "input": {
            "a": 8,
            "b": 12
        },
        "output": 4
    },
    {
        "input": {
            "a": 48,
            "b": 18
        },
        "output": 6
    },
    {
        "input": {
            "a": 48,
            "b": 12
        },
        "output": 12
    },
    {
        "input": {
            "a": -48,
            "b": 12
        },
        "output": 12
    },
    {
        "input": {
            "a": 48,
            "b": 0
        },
        "output": 48
    }
]


def euclidean(a, b):
    """
    Time complexity: O(k) - k number of time we have to divide until we get 0
    Space complexity: O(k) - k number of time we have to divide until we get 0
    """
    assert a == int(a) and b == int(b), "The numbers must be integer only!"

    if a < 0:
        a = -1 * a

    if b < 0:
        b = -1 * b

    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high
    remainder = high % low
    return euclidean(low, remainder)


if __name__ == "__main__":
    for test in tests:
        result = euclidean(**test["input"])
        assert result == test["output"], f"Expected: {test['output']} but got {result}"
