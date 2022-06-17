# Questions: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

tests = [
    {
        "input": [0, 0, 1, 0],
        "output": 2
    },
    {
        "input": [0, 0, 0, 0],
        "output": 2
    },
    {
        "input": [0, 1, 0, 0, 0, 0],
        "output": 3
    },
    {
        "input": [0, 1, 0],
        "output": 1
    },
    {
        "input": [0, 0, 1, 0, 0, 1, 0, 0],
        "output": 5
    },
    {
        "input": [0, 0, 0, 0, 1, 0, 0],
        "output": 4
    },
    {
        "input": [0, 0],
        "output": 1
    }
]


def jumpingOnClouds(c):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    count = 0
    index = 0
    while index < len(c): # go to the end of the elements
        if index + 2 < len(c) and c[index+2] == 0:
            count += 1
            index += 2
        else:
            if index + 1 < len(c) and c[index + 1] == 0:
                count += 1
            index += 1
    return count


def jumpingOnCloudsSol2(c):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    if len(c) == 1: return 0
    if len(c) == 2: return 0 if c[1] == 1 else 1

    if c[2] == 1:
        return 1 + jumpingOnCloudsSol2(c[1:])
    else: # c[2] == 0
        return 1 + jumpingOnCloudsSol2(c[2:])


if __name__ == "__main__":
    count = 0
    for test in tests:
        expected = test["output"]
        result = jumpingOnClouds(test["input"])
        if expected != result:
            raise Exception(f"Expected: {expected} but got {result}")
        else:
            count += 1

    print(f"{count} test case passed out of {len(tests)}")

    count = 0
    for test in tests:
        expected = test["output"]
        result = jumpingOnCloudsSol2(test["input"])
        if expected != result:
            print(test['input'])
            raise Exception(f"Expected: {expected} but got {result}")
        else:
            count += 1

    print(f"{count} test case passed out of {len(tests)}")