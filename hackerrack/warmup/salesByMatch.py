# Question: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def count_pair(socks_dict):
    """
    calculate the number of pair
    Time complexity: O(N)
    Space complexity: O(1)
    """
    count = 0
    for key in socks_dict:
        num_of_pair = socks_dict[key] // 2
        count += num_of_pair
    return count


def sockMerchant(ar):
    # Write your code here
    socks_occurrence_dict = {}
    for color in ar:
        # we've seen this sock before
        if color in socks_occurrence_dict:
            socks_occurrence_dict[color] += 1
        else:
            socks_occurrence_dict[color] = 1

    return count_pair(socks_occurrence_dict)


if __name__ == "__main__":
    tests = [
        # only 1 input
        {
            "input": [1],
            "output": 0
        },
        # no match, all socks are unique
        {
            "input": [1, 2, 3],
            "output": 0
        },
        # no socks
        {
            "input": [],
            "output": 0
        },
        # only one kind of socks
        {
            "input": [1, 1, 1, 1, 1],
            "output": 2
        },
        {
            "input": [1, 2, 1, 1, 2, 2, 1, 2, 1],
            "output": 4
        }
    ]

    count = 0
    for test in tests:
        expected = test["output"]
        result = sockMerchant(test["input"])
        if expected != result:
            raise Exception(f"Expected: {expected} but got {result}")
        else:
            count += 1

    print(f"{count} test case passed out of {len(tests)}")
