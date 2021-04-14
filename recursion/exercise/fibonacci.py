# Fibonacci Sequence
# 0 1 1 2 3 5 8 13 .....
# 0 1 2 3 4 5 6 7 ......


def fib_rec(n):
    """
    Time complexity: O(2^n)
    Space complexity: O(2^n)
    """
    if n <= 1: return n
    return fib_rec(n-1) + fib_rec(n-2)


def fib_iter(n):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    a, b = 0, 1

    while n > 0:
        a, b = b, a + b
        n -= 1

    return a


def fib_opt(n):
    """
    Time complexity: O(N)
    """
    if n <= 1:
        return n

    if n in lookup:
        return lookup[n]
    lookup[n] = fib_opt(n-1) + fib_opt(n-2)
    return lookup[n]


if __name__ == "__main__":
    print(fib_rec(7))
    print(fib_iter(7))

    lookup = {}
    print(fib_opt(7))