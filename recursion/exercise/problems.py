def fun(x):
    # fun(5) => 0 1 2 0 3 0 1 4 0 1 2 0
    if (x > 0):
        x -= 1
        fun(x)
        print(x, end=" ")
        x -= 1
        fun(x)


def f( a, n):
    # fun([12, 10, 30, 50, 100], 5)
    print(f"n -> {n}")
    if(n == 1):
        return a[0]
    x = f(a, n - 1)

    print(f"n -> {n}, x -> {x}")
    if(x > a[n - 1]):
        return x
    return a[n - 1]


if __name__ == "__main__":
    a = [1, 5, 8, 2, 3]
    n = 5
    print(f(a, n))