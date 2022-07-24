tests = [
    {
        "input": 2,
        "output": 4
    },
    {
        "input": 0,
        "output": 1
    },
    {
        "input": 4,
        "output": 16
    },
    {
        "input": 1,
        "output": 2
    }
]


def power_of_two_rec(n):
    if n == 0:
        return 1
    return 2 * power_of_two_rec(n-1)


def power_of_two_iter(n):
    result = 1
    while n > 0:
        result *= 2
        n -= 1
    return result


if __name__ == "__main__":
    for test in tests:
        result_iter = power_of_two_iter(test["input"])
        assert (result_iter == test["output"])

        result_rec = power_of_two_rec(test["input"])
        assert (result_rec == test["output"])