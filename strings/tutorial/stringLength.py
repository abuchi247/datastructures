# Constraints
# Length of a string cannot be negative. Can return value 0 to N (size of the string)

def get_length(string):
  """
  Gets the length of the input
  """
  size = 0

  if string is None:
    return size

  for value in string:
    size += 1
  
  return size



if __name__ == '__main__':
  string = "My name is abuchi"
  print(f"{string} = {get_length(string)} length")

  string = ""
  print(f"{string} = {get_length(string)} length")

  string = None
  print(f"{string} = {get_length(string)} length")