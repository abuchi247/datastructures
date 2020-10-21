# Print the bits in an integer starting from the most significant bit (MSB) to the least
# significant bit (LSB). Also known as the leftmost to the right most

# Example
# 1011

# using left shift
#   assuming the numbers are 8 bit long
#   k = 1
#   output = 0
#   while k > 8:
#       check_bit = 1 << (8-k)
#       and_bit = 0 if n & check_bit == 0 else 1
#       output += 10 * and_bit
#       k += 1
#   return output

# using right shit
# output = ""
# while n > 0:
#   bit_value = 1 if n & 1 == 1 else 0
#   output = bitvalue + output
#   n = n >> 1
# return output


def print_bits_sol1(n):
    """
    Using the left shit operator, display the binary representation
    of the number specified
    :param n:
    :return:
    """
    k = 1
    output = 0
    check_bit = 1 << 8 - 1 # 1000 0000 -> shift left to get the start bit
    while check_bit > 0:
        and_value = 1 if n & check_bit != 0 else 0
        output = (10 * output) + and_value
        check_bit = check_bit >> 1  # shift bit to right
    return output


def print_bits_sol2(n):
    """
    Using the left shit operator, display the binary representation
    of the number specified
    :param n:
    :return:
    """
    output = ""
    while n > 0:
        bit_value = n & 1
        output = str(bit_value) + output
        n = n >> 1
    return output


if __name__ == "__main__":
    tests = [1000, 5, 4, 3, 2, 1]
    for i in tests:
        print(f"test: {i} is sol1: {print_bits_sol1(i)}, sol2: {print_bits_sol2(i)}")