# Combination
# N! / (N-R)! * R!

def nCr(n, r):
    num = fact(n)
    den = fact(r) * fact(n-r)

    return num / den


def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n


def NCR(n, r):
    if n == r or r == 0:
        return 1

    return NCR(n-1, r-1) + NCR(n-1, r)


if __name__ == "__main__":
    print(nCr(4, 2))
    print(NCR(4, 2))