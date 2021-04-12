# Indirect recursion: Is when they are one or more functions calling each other recursively in a circular fashion

# Example:
# funcA(n):
#   if n > 0:
#       print(n)
#       funcB(n-1)

# funcB(n):
#   if n > 1:
#       print(n)
#       funcA(n/2)

def funcA(n):
    if n > 0:
        print(n, end=" ")
        funcB(n-1)

def funcB(n):
    if n > 1:
        print(n, end=" ")
        funcA(n//2)


if __name__ == "__main__":
    funcA(20)