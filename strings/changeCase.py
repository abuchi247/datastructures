def change_case(string):
    string_list = list(string)

    for i in range(len(string_list)):
        if 65 <= ord(string_list[i]) <= 90:
            string_list[i] = chr(ord(string_list[i]) + 32)
        elif 97 <= ord(string_list[i]) <= 122:
            string_list[i] = chr(ord(string_list[i]) - 32)

    return "".join(string_list)


if __name__ == "__main__":
    name = "AbUcHi"
    print(change_case(name))