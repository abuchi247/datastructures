# Given two numbers where the individual digits in the numbers are in an array or a list add them
# to get the final result in the same list or array form

# EXAMPLE: using arrays: [1, 2]. The most significant digit is at the 0th index and the least significant digit is
# at index at digit position.
# [1, 2] + [2, 3] = [3, 5]
# [1, 9, 9] + [2] = [2,0,1]

def add_numbers(a, b):
    if a is None or b is None: return None
    if len(a) == 0: return b
    if len(b) == 0: return a

    a_idx = len(a) - 1
    b_idx = len(b) - 1
    result = []
    carry = 0
    digit = 0
    total = 0

    while a_idx >= 0  and b_idx >= 0:
        total = carry + a[a_idx] + b[b_idx]
        digit = total % 10
        carry = total // 10
        result.insert(0, digit)  # insert the value to the beginning of the array
        a_idx -= 1
        b_idx -= 1

    # ensure there's no low hanging fruit on array 1
    while a_idx >= 0:
        total = carry + a[a_idx]
        digit = total % 10
        carry = total // 10
        result.insert(0, digit)
        a_idx -= 1

    # ensure there's no low hanging fruit on array 1
    while b_idx >= 0:
        total = carry + b[b_idx]
        digit = total % 10
        carry = total // 10
        result.insert(0, digit)
        b_idx -= 1

    if carry != 0: # for situation where is still value to be carried over
        result.insert(0, carry)
    return result


if __name__ == "__main__":
    a, b = [1,2], [2, 3]
    print(add_numbers(a, b))

    a, b = [1, 9, 9], [2]
    print(add_numbers(a, b))

    a, b = [1, 2, 7], [4, 4]
    print(add_numbers(a, b))

    a, b = [9, 9, 9], [1]
    print(add_numbers(a, b))
