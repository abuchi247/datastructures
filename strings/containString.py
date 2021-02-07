# Constraints and assumptions
# Target and source strings can only be strings


def strstr(source, target):
  """
  Gets the length of the input
  """
  if source is None or target is None:
    return False

  if not isinstance(source, str):
    return False

  if not isinstance(target, str):
    return False

  if len(target) > len(source):
    return False

  index = 0
  target_length = len(target)

  while index < len(source):
    boundary = index + target_length
    if boundary > len(source):
      return False
    new_str = source[index:boundary]
    if new_str == target:
      return True
    index += 1

  return False


if __name__ == "__main__":
    print(strstr("GeeksForGeeks", "Fr"))
    print(strstr("GeeksForGeeks", "For"))
    print(strstr("s", "s"))
