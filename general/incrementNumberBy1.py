# Suppose that you invest your own numeral system (which is neither decimal, binary, nor any of the common
# ones). You specify the digits and the order of the digits in that numeral system

# Write a function that increments the number by 1 and return the result

# Consider that the numeral system that you set is
# A, B, C, D

# These are the only valid digits in the numbers and
# A < B < C < D

# Example
# ABB => ABC
# ACD => ADA
# ADD => BAA
# DDD => AAAA

def increment_digit(original_numbers):
    allowed_digits = ['A', 'B', 'C', 'D']    # Allowed digits
    # check if the digits are valid
    for digit in original_numbers:
        # ensure the digits are valid
        if digit is None:
            return None

        if digit not in allowed_digits:
            return None

    increased_number = original_numbers[:]

    current_index = len(original_numbers) - 1

    increment_complete = False

    while current_index >= 0 and not increment_complete:
        current_digit = original_numbers[current_index]   # gets the current character

        index_current_digit = allowed_digits.index(current_digit)

        index_of_next_digit = (index_current_digit + 1) % len(allowed_digits)   # get the next index

        # update the old value
        increased_number[current_index] = allowed_digits[index_of_next_digit]

        if index_of_next_digit != 0:    # no carry over happening
            increment_complete = True

        # if we are the most significate digit and it wraps around. Just like 9 + 1 = 10
        if current_index == 0 and index_of_next_digit == 0: 
            increased_number.insert(0, allowed_digits[0]) # in the case of DDD + 1 => AAAA

        current_index -= 1

    return increased_number

if __name__ == "__main__":
    digits = [
        ['A', 'B', 'B'],
        ['A', 'C', 'D'],
        ['A', 'D', 'D'],
        ['D', 'D', 'D']
    ]

    for digit in digits:
        print(f"{digit} -> {increment_digit(digit)}")




