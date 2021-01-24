# https://leetcode.com/problems/backspace-string-compare/

# Given two strings S and T, return if they are equal when both are typed 
# into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

# Constraints:
# Will it always be strings? yes
# Is the strings case sensitive? yes
# What happens when more than one # is found consecutively?
  # Delete the previous characters matching the number of # found
# What happens when # is entered on an empty string? Nothing
# What happens if both strings are empty? Then they match

# Test cases
# "ab##"", "" -> True
# "abc", "abb#cc#" -> True
# "##", "ab##" -> True
# 
# s = "ab#c"
# t = "ad#c"  

def load_stack(string):
    stack = []

    for x in string:
        if x == "#":
            # nothing to remove
            if len(stack) == 0:
                continue
            else:   # remove previous added item
                stack.pop()
        else:
            # add to stack
            stack.append(x)

    return stack

def brute_force(s, t):
    # Time Complexity: N + M
    # Space Complexity: N + M
    
    s_stack = load_stack(s)
    t_stack = load_stack(t)

    # check if they both have the same length
    if len(s_stack) != len(t_stack):
        return False

    # check all the elements
    while len(s_stack) > 0 and len(t_stack) > 0:
        if s_stack.pop() != t_stack.pop():
            return False
    return True
    

if __name__ == "__main__":
  s = "ab#c"
  t = "ad#c"
  print(brute_force(s, t))

  s = "aaa#"
  t = "aa#"
  print(brute_force(s, t))

  s = "a##c"
  t = "#a#c"
  print(brute_force(s, t))

  s = "xywrrmp"
  t = "xywrrmu#p"
#   print(backspaceCompare(s, t))
  print(brute_force(s, t))

  s = ""
  t = "abuc####"
  print(brute_force(s, t))

  s = "ABUC"
  t = "abuc"
  print(brute_force(s, t))