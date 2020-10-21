# Get the nth bit
# Check the nth bit in an integer and return 1 if the bit at nth position is 1 and 0 if the bit is 0

# Pseudo code
# How do we identify the bit at nth position?
# We use integer 1 to help in identifying bit at nth position
               # 7 6 5 4 3 2 1 0 -> positions
# example -> b = 1 0 0 1 0 0 1 1
# integer 1 =    0 0 0 0 0 0 0 1  AND operator performed
# and_bit =      0 0 0 0 0 0 0 1

# get the bit at position 0
#  Using the AND bit operator (&)
#  We need a check_bit to use to compare the original bit
# n = 0 => position
# Use the shift left bit operation to manipulate the check bit to the position we want to check
# check_bit = 1 << n

# For example -> position 1
#         b = 1 0 0 1 0 0 1 1
# check_bit = 0 0 0 0 0 0 1 0
# and_bit   = 0 0 0 1 0 0 1 0 => after AND operator
# check if and_bit == check_bit => if so, return 1 else 0

def get_nth_bit(num, bit_pos):
    """
    gets the bit at position n
    :param num: integer value to check
    :param bit_pos: is the position of the bit
    :return: 1 if bit at position n is 1 or 0 if bit at postion n is 0
    """
    # construct my check bit
    check_bit = 1 << bit_pos  # using the shift left bit operator to manipulate the postion or bit in the check bit
    and_bit = num & check_bit   # stores the result after performing the AND bit operator on num and check_bit

    return 1 if and_bit == check_bit else 0


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

            print(f"Bit at position {bit_pos} is {get_nth_bit(N, bit_pos)}")
            num_test_cases -= 1
    except (ValueError, TypeError) as ex:
        raise ex