# factorial of a number
# N! = 1 * 2 * 3 * ..... * N
# 5! = 1 * 2 * 3 * 4 * 5


def fact_rec(n):
    if n == 0:
        return 1
    return fact_rec(n-1) * n

def fact_iter(n):
    total = 1

    while n > 0:
        total *= n
        n -= 1
    return total


if __name__ == "__main__":
    print(fact_iter(5))
    print(fact_rec(5))