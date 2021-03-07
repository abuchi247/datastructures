# Reverse the bits in an array
# example:
# 10111 (23) = 11101 (29)
# 0011 (3) = 1100 (12)
# 0100 (4) = 0010 (2)

def reverseBits(N):
  reverse_num = 0

  for i in range(32):
    last_bit = N & 1
    reverse_num = reverse_num << 1
    reverse_num = reverse_num | last_bit
    N >>= 1
  return reverse_num


if __name__ == "__main__":
  N = 3
  print(reverseBits(N))
