# The OR (|) operator performs the or operator on every bit of 2 numbers
# the output bit is set to 1 when one of the bit is set to 1 in the bit being compared

x = ord('A')    # 01000001
y = ord('L')    # 01001100
z = x | y       # 01001101

print(f"A: {x} | L: {y} = {z}")
print(bin(z))