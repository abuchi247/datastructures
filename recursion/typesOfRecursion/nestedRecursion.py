# Nest recursion is a function that calls itself as a recursive call passing itself as a parameter

# func(n):
#   ......
#   func(func(n-1))

def func(n):
    if n > 100:
        return n - 10
    return func(func(n + 11))

if __name__ == "__main__":
    print(func(95))