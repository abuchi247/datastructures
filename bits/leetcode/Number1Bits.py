# write a function that takes an unsigned integer and return the number of '1' bits it has
# Also known as the Hamming weight

def hamming_weight(N):
    """
    Returns the number of '1' bit in the 32 bit int passed
    Big O(N)
    :param N:
    :return:
    """
    count = 0

    while N > 0:
        last = int(N % 10)  # get the right most value in the integer
        if last & 1 == 1: # check if the right most bit is 1
            count += 1
        N /= 10    # Store the remain values excluding the last
    return count

def hammingWeight(N: int) -> int:
    """
    Returns the number of '1' bit in the 32 bit int passed using observation approach
    Big O(LogN)
    :param N:
    :return:
    """
    count = 0

    while N:
        count += 1
        N = N & (N-1)
    return count


def hammingWeightSol2(N: int) -> int:
    """
    Returns the number of '1' bit in the 32 bit int passed. Using right shift approach
    Big O(Log N)
    :param N:
    :return:
    """
    count = 0

    while N:
        if N & 1 == 1:
            count += 1
        N >>= 1

    return count


if __name__ == "__main__":
    T = int(input("Number of test cases: "))

    while T > 0:
        N = int(input("Enter a number: "))
        print(hamming_weight(N))
        print(hammingWeight(N))
        print(hammingWeightSol2(N))
        T -= 1