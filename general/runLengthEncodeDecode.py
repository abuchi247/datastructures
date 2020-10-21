# Write a program which encodes a string using run - length encoding and decodes a string encoded using
# run - length encoding

# Example:
# "ABBCCC" -> 1A2B3C
# "A" -> 1A
# "1D2E1F" -> DEEF

def run_length_encode(original_string):
    if original_string is None:
        return None

    # index of the current string
    cur_index = 0
    encoded_string = "" # result of the encoded string
    while cur_index < len(original_string): # loop through the strings character by character
        cur_char = original_string[cur_index]   # get the current character
        num = 0 # store the count of that string
        compare_index = cur_index
        # walks right in front of the current index until the characters don't match anymore
        while compare_index < len(original_string) and cur_char == original_string[compare_index]:
            compare_index += 1
            num += 1    # keep track of the occurance of repeatation

        encoded_string += str(num) + cur_char   # append the number of times the charact appears then the character

        cur_index = compare_index   # move on to the next character

    return encoded_string


def repeat_char(char, times):
    new_str = ""
    for _ in range(times):
        new_str += char

    return new_str


def run_length_decode(encoded_string):
    """
    Handles situation whereby the number takes more than 1 space
    e.g 19A3B
    :param encoded_string:
    :return:
    """
    if encoded_string is None:
        return None

    decoded_string = ""

    index = 0
    while index < len(encoded_string) - 1:
        num_occurance = ""  # store the occurance value
        while encoded_string[index].isdigit():  # keep walking the string until we find a letter
            num_occurance += encoded_string[index]  # append the character in the num_occurance variable
            index += 1  # increment index
        character = encoded_string[index]   # get the letter in the string
        decoded_string += repeat_char(character, int(num_occurance))    # generate a repeated char based on its occurance
        index += 1
    return decoded_string

if __name__ == "__main__":
    string = "ABBCCC"
    encode = run_length_encode(string)
    print(encode)
    print(run_length_decode(encode))

    string = "AAAAAAAAAAAAAAAAA"
    encode = run_length_encode(string)
    encode = "19A3B"
    print(encode)
    print(run_length_decode(encode))
    encode = "1a22b7c"
    print(encode)
    print(run_length_decode(encode))