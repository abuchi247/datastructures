# check if a given string is palindrome

# Handle different data types
# if string is None
# Check if empty
# cannot have more than 1000 X 2 element in length
# spaces are not considered
# check is case insensitive

def is_palindrome(string):
    if string is None:
        return False

    if not isinstance(string, str):
        print("{} must be a string".format(str(string)))
        return False

    index = 0   # start from the beginning to the end
    last_index = len(string) - 1    # start from the end and walk to the front
    string = string.lower()     # convert the string elements to lowercase

    while index < last_index:
        forward_char = string[index]    # forward character
        backward_char = string[last_index]  # back character

        while forward_char == " ":  # skip over the white space
            index += 1
            forward_char = string[index]

        while backward_char == " ": # skip over the white space
            last_index -= 1
            backward_char = string[last_index]

        if forward_char != backward_char:
            return False

        index += 1
        last_index -= 1

    return True


# def is_palindrome_rec(string, start, end):
#     if string is None:
#         return False
#
#     if not isinstance(string, str):
#         print("{} must be a string".format(str(string)))
#         return False
#
#     # base case
#     if start > end:
#         return True
#
#     if string[start] != string[end]:
#         return False
#
#     return is_palindrome_rec(string, start+1, end-1)


if __name__ == "__main__":
    test_cases = ["", "123", 123, [123], "2", "radar", None, "abba", "a  b b a ", "ABa", "a     "]

    for test in test_cases:
        word = "is" if is_palindrome(test) else "is NOT"
        print("{} {} a parlindrome".format(str(test), word))
