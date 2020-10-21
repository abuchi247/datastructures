# Implement the string concatenation method whereby
# the src string is appended to the destination string and returns
# the index of the src string in the destination string


def strcat(dest, src):
    if dest is None:
        return None
    if src is None:
        return None

    if not isinstance(dest, str):
        return None
    if not isinstance(src, str):
        return None

    return dest + src

if __name__ == "__main__":
    print(strcat("abuchi ", "obiegbu"))
    print(strcat("abuchi", 123))
    print(strcat(None, "abuchi"))
    print(strcat("", ""))