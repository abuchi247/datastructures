# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in
# their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]

def countBits(num: int):
    """
    returns an array of size num, with a count of the set bit of every index
    :param num:
    :return:
    """
    arr = []

    for i in range(num + 1):
        arr.append(count_set_bits(i))
    return arr


def count_set_bits(N):
    """
    Returns the number of set bit in N

    Big O(logN)
    space = 1
    :param N:
    :return:
    """

    count = 0

    while N:
        count += 1
        N = N & (N-1)
    return count


if __name__ == "__main__":
    T = int(input("Number of testcases: "))

    while T > 0:
        N = int(input("Enter a number: "))
        print(countBits(N))
        T -= 1