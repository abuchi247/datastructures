#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def generate_password_sol1(n_letters, n_symbols, n_numbers):
    password = ""

    # get the random letters first
    for _ in range(n_letters):
        password += letters[random.randint(0, len(letters)-1)]

    # get the random symbols second
    for _ in range(n_symbols):
        password += symbols[random.randint(0, len(symbols) - 1)]

    # get the random numbers last
    for _ in range(n_numbers):
        password += numbers[random.randint(0, len(numbers) - 1)]

    print(password)
    return password

def generate_password_sol2(n_letters, n_symbols, n_numbers):
    password = []

    # get the random letters first
    for _ in range(n_letters):
        password.append(letters[random.randint(0, len(letters)-1)])

    # get the random symbols second
    for _ in range(n_symbols):
        password.append(symbols[random.randint(0, len(symbols) - 1)])

    # get the random numbers last
    for _ in range(n_numbers):
        password.append(numbers[random.randint(0, len(numbers) - 1)])

    # shuffle the array
    random.shuffle(password)

    new_password = "".join(password)
    print(new_password)

    return new_password
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

if __name__ == "__main__":
    generate_password_sol1(nr_letters, nr_symbols, nr_numbers)
    generate_password_sol2(nr_letters, nr_symbols, nr_numbers)