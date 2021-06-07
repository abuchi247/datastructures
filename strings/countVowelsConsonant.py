# convert all the characters to upper case or lower case
# store all the vowels in a variable
# check if each value is a valid alphabet


def count_vowels_and_consonants(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    vcount = 0
    ccount = 0

    string_list = list(string)

    for i in range(len(string_list)):
        character = string_list[i].lower()
        if 97 <= ord(character) <= 122:     # character is between a - z
            if character in vowels:
                vcount += 1
            else:
                ccount += 1

    print(f"{string_list} contains {vcount} vowels and {ccount} consonants.")


def count_words(string):
    word = 0

    for i in range(len(string)-1):
        if string[i] == " " and string[i+1] != " ":
            word += 1

    # i = 0
    # while i < len(string):
    #     if string[i] == " ":
    #         j = i+1
    #         while string[j] == string[i]:
    #             j += 1
    #         word += 1
    #         i = j
    #         continue
    #     i += 1

    print(f"{string} contains {word+1} words")


if __name__ == "__main__":
    string = "How are you  u"

    count_vowels_and_consonants(string)
    count_words(string)