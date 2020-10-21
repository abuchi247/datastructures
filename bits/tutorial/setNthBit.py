# Set the nth bit to 1
# change the nth bit of a number

# Pseudo code
# Using the check_bit to compare the bits in the number to the checkbit
# Generate the check_bit using the shift left bit operation on number 1
# Perform the OR bit operation on the check_bit and the number we want to change the bit
# store and the return the output of the or operation

# Example
# number = 1 0 0 1 0 0 1 1
#     n =  1

# number    =          1 0 0 1 0 0 1 1
# check bit = 1 << n = 0 0 0 0 0 0 1 0
# or_bit             = 1 0 0 1 0 0 1 0

def set_nth_bit_to_1(num, n):
    """
    Sets the nth bit at postion n to 1
    :param num: number to change the nth bit
    :param n: position of the number to be changed
    :return: new number with the changed position
    """
    set_bit = 1 << n    # construct the set bit using the shift left operator
    result = num | set_bit  # store the result of the OR bit operation which will force the bit at position n to be 1
    return result

def set_nth_bit_to_0(num, n):
    """
    Sets the nth bit at postion n to 0
    :param num: number to change the nth bit
    :param n: position of the number to be changed
    :return: new number with the changed position
    """
    set_bit = ~(1 << n)    # construct the set bit using the shift left operator and performing the NOT (Flip) bit operation
    result = num & set_bit  # store the result of the AND bit operation which will force the bit at position n to be 0
    return result


if __name__ == "__main__":
    # 147 = 1 0 0 1 0 0 1 1
    print(set_nth_bit_to_1(147, 1))
    print(set_nth_bit_to_0(147, 1))