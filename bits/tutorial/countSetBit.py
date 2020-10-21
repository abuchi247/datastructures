# Given a number N and find number of set bits in it


# N => integer number
#  Example:
#   N = 12 (1100)  output: 2
#   N = 11 (1011)  output: 3

# Pseudo code
# count_set_bit(N)
#   count = 0   # store number of set bits
#   Assumption we only have 8 bit in an integer
#   while n > 0:
#       if N & 1 == 1:  # bit is set
#           count += 1
#       N = N >> 1 # shift right by 1. Dividing N by 2 Log(N)
#   return count

def count_set_bit_sol1(N):
    """
    Counts the number of set bit in an integer using the right shift approach
    Big O(number of bits)
    :param N: integer number
    :return: number of set bit count
    """
    count = 0

    while N > 0:
        if N & 1 == 1:
            count += 1
        N = N >> 1  # shift bit one position towards the right
    return count


def count_set_bit_sol2(N):
    """
    Faster solution time as it runs as many times as there are set bits

    Big O(number of 1s)
    :param N:
    :return:
    """
    # while N > 0, we know there's at least one set bit
    # increment count
    # N = N & (N-1)
    #
    # Example N = 8 -> 01000
    # N -1 (8-1 = 7)-> 00111 & operator
    # N = 0            -----
    # N = 0            00000
    count = 0
    while N > 0:
        count += 1
        N = N & (N-1)
    return count


if __name__ == "__main__":
    T = int(input("Number of test cases: "))

    while T > 0:
        N = int(input("Enter number to get set bit count: "))
        print(f"Set bit count of {N} = {count_set_bit_sol1(N)}")
        print(f"Set bit count of {N} = {count_set_bit_sol2(N)}")
        T -= 1