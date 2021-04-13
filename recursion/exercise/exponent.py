# Exponent (M) ^ n

# 2 ^ 5 = 2 * 2 * 2 * 2 *2 2

def pow(m, n):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    if n == 0:
        return 1
    return pow(m, n-1) * m


def pow_optimize(m, n):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """
    if n == 0:
        return 1

    if n % 2 == 0:
        return pow(m*m, n//2)
    return m * pow(m*m, n//2)


def pow_iter(m, n):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """
    total = 1

    if n == 0:
        return total

    for _ in range(n):
        total *= m

    return total


if __name__ == '__main__':
    print(pow(2, 8))
    print(pow_optimize(2, 8))
    print(pow_iter(2, 8))