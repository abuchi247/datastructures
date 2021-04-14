# Permutation
# N! / (N-R)!

def nPr(n, r):
    num = fact(n)
    den = fact(n-r)

    return num / den


def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n


if __name__ == "__main__":
    print(nPr(10, 4))