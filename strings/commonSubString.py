def commonSubstring(a, b):
  a_list = a.split()
  b_list = b.split()

  min_size = min(len(a_list), len(b_list))

  for i in range(min_size):
    set_a = set(a_list[i])
    found_matching_substring = False
    for ch in set_a:
      if ch in b_list[i]:
        found_matching_substring = True
        break
    output = "YES" if found_matching_substring else "NO"
    print(output)

  #  there are remain words on a list
  if min_size < len(a_list):
    for _ in range(min_size, len(a_list)):
      print("NO")

  if min_size < len(b_list):
    for _ in range(min_size, len(b_list)):
      print("NO")
    

if __name__ == "__main__":
  a = "hello hi"
  b = "world bye"

  commonSubstring(a, b)