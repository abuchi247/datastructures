# Head Recursion: is a function that performs no task at the beginning of the function execution. Hence, the recursive
# must be the first action that is performed during the function exection. Every action is performed at the return of the
# recursive call.
# Head Recursion cannot be easily be transformed into a loop

# Example:
# func(n):
#   if n > 0:
#       func(n-1)
#       print(n)


def func(n):
    if n > 0:
        func(n - 1)
        print(n, end=" ")


def func_iterative(n):
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1


if __name__ == "__main__":
    func(3)
    print()
    func_iterative(3)
