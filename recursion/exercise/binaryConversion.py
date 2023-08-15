tests = [
    {
        "input": 4,
        "output": "100"
    },
    {
        "input": 1,
        "output": "1"
    },
    {
        "input": 3,
        "output": "11"
    },
    {
        "input": 10,
        "output": "1010"
    }
]


def convert_binary(num):
    """
    Time and space complexity O(log(n))
    """
    assert int(num) == num, "The parameter must be an integer only!"
    if num == 0:
        return ""

    return convert_binary(num // 2) + f"{num % 2}"


def convert_binary_iter(num):
    """
    Time and space complexity O(log(n))
    """
    assert int(num) == num, "The parameter must be an integer only!"
    output = ""

    while num > 0:
        output = str(num % 2) + output
        num //= 2

    return output


if __name__ == "__main__":
    for test in tests:
        result = convert_binary(test["input"])
        if result != test["output"]:
            raise Exception(f"Expected: {test['output']} got {result}")
        result = convert_binary_iter(test["input"])
        if result != test["output"]:
            raise Exception(f"Expected: {test['output']} got {result}")
