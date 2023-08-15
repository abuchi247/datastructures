# factorial of a number
# N! = 1 * 2 * 3 * ..... * N
# 5! = 1 * 2 * 3 * 4 * 5

tests = [
    {
        "input": 0,
        "output": 1
    },
    {
        "input": 1,
        "output": 1
    },
    {
        "input": 2,
        "output": 2
    },
    {
        "input": 3,
        "output": 6
    },
    {
        "input": 4,
        "output": 24
    }
]


def fact(n):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    assert 0 <= n == int(n), 'The number must be positive integer only!'

    if n in [0, 1]:
        return 1
    return n * fact(n-1)


if __name__ == "__main__":
    for test in tests:
        result = fact(test["input"])
        assert result == test["output"]