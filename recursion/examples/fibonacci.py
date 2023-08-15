def fib_head(n):
    assert 0 <= n == int(n), 'The number must be 0 or more and integer'
    if n in [0, 1]:
        return n

    return fib_head(n - 1) + fib_head(n - 2)


def fib_tail(n, a=0, b=1):
    assert 0 <= n == int(n), 'Fibonacci number cannot  must be 0 or more and integer'
    if n == 0:
        return a
    if n == 1:
        return b

    return fib_tail(n - 1, b, a + b)


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


print(fib_head(10))
print(fib_tail(10))

