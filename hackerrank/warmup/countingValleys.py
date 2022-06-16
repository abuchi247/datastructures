# Questions: https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

tests = [
    {
        "input": "DDUUUUDD",
        "output": 1
    },
    {
        "input": "UDDDUDUU",
        "output": 1
    },
    {
        "input": "UD",
        "output": 0
    },
    {
        "input": "DUDUDU",
        "output": 3
    },
    {
        "input": "UDUDUD",
        "output": 0
    }
]


def countingValleys(steps, path):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    direction = 0
    in_valley = False
    num_valleys = 0
    for i in range(steps):
        if path[i] == "D":
            direction -= 1
        else:
            direction += 1

        if direction < 0:
            in_valley = True
        elif direction > 0:
            in_valley = False
        else: # direction is 0
            if in_valley:
                num_valleys += 1
    return num_valleys


if __name__ == "__main__":
    count = 0
    for test in tests:
        expected = test["output"]
        result = countingValleys(len(test["input"]), test["input"])
        if expected != result:
            raise Exception(f"Expected: {expected} but got {result}")
        else:
            count += 1

    print(f"{count} test case passed out of {len(tests)}")
