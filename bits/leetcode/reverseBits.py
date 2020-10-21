# Reverse the order of bits in an integer

# 100101 -> 101001

# check_bit = 1
# new_value = 0
# while N > 0:
#    cur_bit = check_bit & N
#    new_value = new_value << 1 | cur_bit
#    N = N >> 1


def reverse_bit(num):
    reverse_num = 0
    while num != 0:
        last_bit = num & 1 # get the right most bit (LSB)
        reverse_num = reverse_num << 1  # shift left to make room for the last bit to be inserted
        reverse_num = reverse_num | last_bit    # insert the last bit to the right most position
        num = num >> 1  # shift original number to the right

    return reverse_num

if __name__ == "__main__":
    num = 11
    print(bin(num))
    print(bin(reverse_bit(num)))