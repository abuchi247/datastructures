def reverse_iter(string):
  """
  reverses a string using iterative approach
  Big O(N)
  Space complexity O(N)
  """
  new_str = ""
  for i in range(len(string)-1, -1, -1):
    new_str += string[i]

  return new_str

def reverse_rec(string):
  if len(string) <= 1:
    return string

  return reverse_rec(string[1:]) + string[0]


def main():
  T = int(input("How many test cases do you plan to run? "))

  while T > 0:
    input_str = input("Enter a string to reverse: ")

    print(f"Before reversing string: {input_str}")
    if reverse_iter(input_str) != reverse_rec(input_str):
      print("One of your implementation is wrong")
      print(f"Iterative: {reverse_iter(input_str)}")
      print(f"Recursive: {reverse_rec(input_str)}")
    print(f"After reversing string: {reverse_iter(input_str)}")
    T -= 1

if __name__ == "__main__":
  main()