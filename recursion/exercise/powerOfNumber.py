# How to calculate power of a number using recursion?
# base^exp = base * base * base * .... (exp times)

tests = [
    {
        "input": {
            "base": 2,
            "exp": 0
        },
        "output": 1
    },
    {
        "input": {
            "base": 2,
            "exp": 3
        },
        "output": 8
    },
    {
        "input": {
            "base": 2,
            "exp": 1
        },
        "output": 2
    }
]


def power(base, exp):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    assert exp >= 0 and exp == int(exp), "The exponent must be positive integer only!"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp-1)


# def power_opt(base, exp):
#     """
#     Time complexity: O(N)
#     Space complexity: O(N)
#     """
#     assert exp >= 0 and exp == int(exp), "exp needs to be 0 or more and must be integer!"
#     if exp == 0:
#         return 1
#
#     if exp % 2 == 0:
#         x = power_opt(base, exp//2)
#         return x * x
#     else:
#         x = power_opt(base, exp-1)
#         return x


if __name__ == "__main__":
    for test in tests:
        result = power(**test["input"])
        assert result == test["output"]

