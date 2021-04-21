

def convert_binary(num):
    """
    Time and space complexity O(log(n))
    """
    if num == 0:
        return

    convert_binary(num // 2)
    print(num % 2, end="")


def convert_binary_iter(num):
    """
    Time and space complexity O(log(n))
    """
    output = ""

    while num > 0:
        output = str(num % 2) + output
        num //= 2

    print(output)


if __name__ == "__main__":
    convert_binary(100)
    print()
    convert_binary_iter(100)