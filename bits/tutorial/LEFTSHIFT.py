# The left shift operator (<<) shift left the bits of a number
# starting from the least significant bit (right most bit in this case), it will shift the bits
# using the offset to the left. When an overflow happens, that is when there is not room in the
# left of the output to fit the remaining bits, the remaining bits are lost. The remaining unfilled bits in the
# right-most side of the output bit will be replace with a '0' if it's a positive number or '1' if negative

# Issues
# The OVERFLOW issue
# The FILL is also system dependent, especially for signed numbers

# x = ord('A')    # 01000001
# z = x << 3      # 00001000 shift each bit 3 places to the left

# left shifting means N = N * (2^i)
# N = 65 * (2^3)
# N = 65 * 8
# N = 520


def compute_left_shift(N, offset):
    """
    Computes the left shift of a number N
    N = N * 2^offset -> formular
    :param N: Integer value
    :param offset: bit position to shift
    :return: return new integer value
    """
    new_n = N << offset
    print(f"{N} << {offset} = {new_n}")
    print(f"old bin: {bin(N)}, new binary: {bin(new_n)}")
    return new_n


if __name__ == "__main__":
    try:
        num_test_cases = int(input("How many test cases do you plan to run? "))

         # do below until number of test cases become 0
        while num_test_cases > 0:
            try:
                N, bit_pos = list(
                    map(int, input("Enter value of N and offset of bit to shift (space separated: ").split()))
            except (ValueError, TypeError) as ex:
                raise ex

            compute_left_shift(N, bit_pos)
            num_test_cases -= 1
    except (ValueError, TypeError) as ex:
        raise ex
