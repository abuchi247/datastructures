# The XOR operator (^) performs XOR on every bit of two numbers
# the output is 1 only when one of the two input is exclusively 1
# example: 1 ^ 0 = 1 or 0 ^ 1 = 1

x = ord('A')    # 01000001
y = ord('L')    # 01001100
z = x ^ y       # 00001101

print(f"A: {x} ^ L: {y} = {z}")