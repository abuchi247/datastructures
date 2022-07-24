# https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
tests = [
    {
        "input": ("hello", "world"),
        "output": "YES"
    },
    {
        "input": ("", "world"),
         "output": "NO"
    },
    {
        "input": ("h", "world"),
         "output": "NO"
    },
    {
        "input": ("w", "w"),
         "output": "YES"
    }
]


def twoStrings(s1, s2):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    # Write your code here
    lookup = set(s1)

    for ch in s2:
        if ch in lookup:
            return "YES"
    return "NO"


if __name__ == "__main__":
    count = 0
    for test in tests:
        expected = test["output"]
        result = twoStrings(*test["input"])
        if expected != result:
            raise Exception(f"Expected: {expected} but got {result}")
        else:
            count += 1

    print(f"{count} test case passed out of {len(tests)}")