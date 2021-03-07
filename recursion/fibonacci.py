def fib_head(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  result1 = fib_head(n-1)
  result2 = fib_head(n-2)

  return result1 + result2


def fib_tail(n, a=0, b=1):
  if n == 0:
    return a

  if n == 1:
    return b

  return fib_tail(n-1, b, a+b)

print(fib_head(5))
print(fib_tail(5))