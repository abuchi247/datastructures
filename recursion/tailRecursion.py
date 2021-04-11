# Tail Recursion: is a function that performs no task during return of the recursive call. Hence, the recursive call
# must be the last action performed in the function
# Tail Recursion can easily be transformed into a loop because loops are more efficience space-wise

# Example:
# func(n):
#   if n > 0:
#       print(n)
#       func(n-1)

# NOT A VALID CALL
# func(n):
#   if n > 0:
#       print(n)
#       func(n-1) + n       ---> not valid because the n is performed during the return of the recursive call


def func(n):
    if n > 0:
        print(n, end=" ")
        func(n - 1)


def func_iterative(n):
    while n > 0:
        print(n, end=" ")
        n -= 1


if __name__ == "__main__":
    func(3)
    print()
    func_iterative(3)
