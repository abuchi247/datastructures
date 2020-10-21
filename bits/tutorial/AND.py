# & operator performs and the and operator on every bit of two numbers

x = ord('A')    # 01000001
y = ord('L')    # 01001100
z = x & y   # bitwise and each operator = 01000000

print(f"A: {x} & L: {y} = {z}")