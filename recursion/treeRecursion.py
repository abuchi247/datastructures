# Tree Recursion: is a function that calls itself more than once.


# Example:
# func(n):
#   if n > 0:
#       print(n)
#       func(n-1)
#       func(n-1)


def func(n):
    if n > 0:
        print(n, end=" ")
        func(n - 1)
        func(n-1)


if __name__ == "__main__":
    func(3)
