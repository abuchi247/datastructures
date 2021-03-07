def power(x, n):
    if n == 0: return 1
    # elif n == 1: return x
    result = 1
    for i in range(n):
        result *= x
    return result
    

def power_rec_slow(x, n):
    """
    Time complexity: O(N)
    """
    if n == 0: 
        return 1
    return power_rec_slow(x, n-1)

def power_rec(x, n):
    """
    Time complexity: O(LogN)
    """
    if n == 0: return 1
    # elif n == 1: return x
    elif n % 2 == 0:
        value = power_rec(x, n/2)
        return value * value
    else:
        return power_rec(x, n-1)


print(power(2, 6))