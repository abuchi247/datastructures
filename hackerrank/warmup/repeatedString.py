# https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

tests = [
    {
        "input": {
            "s": "abcac",
            "n": 10,
        },
        "output": 4
    },
    {
        "input": {
            "s": "a",
            "n": 1000,
        },
        "output": 1000
    },
    {
        "input": {
            "s": "cds",
            "n": 1000,
        },
        "output": 0
    },
    {
        "input": {
            "s": "abc",
            "n": 1000,
        },
        "output": 334
    }
]


def repeatedString(s, n):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    num_of_a = s.count('a') # get the number of a (O(N))
    num_of_exact_substring = n // len(s) # O(1)




if __name__ == "__main__":
    count = 0
    for test in tests:
        expected = test["output"]
        result = repeatedString(**test["input"])
        if expected != result:
            raise Exception(f"Expected: {expected} but got {result}")
        else:
            count += 1

    print(f"{count} test case passed out of {len(tests)}")