# The sum of first N natural numbers is the total sum of the numbers start from 1 upto N

# Example:
# N = 7
# 1 + 2 + 3 + 4 + 5 + 6 + 7

def sum_of_first_n_rec(n):
    # Very expensive as it uses stack memory -> space complexity = N
    # Time complexity = O(N)
    if n <= 0:
        return 0
    return sum_of_first_n_rec(n-1) + n


def sum_of_first_n_iter(n):
    # faster than recursion as it uses a constant space complexity = 1
    # Time complexity = O(N)
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


def sum_of_first_n_math(n):
    # Time complexity O(1)
    # Space complexity O(1)
    # Formular: (n(n+1))/2
    return n * (n + 1) // 2


if __name__ == "__main__":
    print(sum_of_first_n_rec(4))
    print(sum_of_first_n_iter(4))
    print(sum_of_first_n_math(4))