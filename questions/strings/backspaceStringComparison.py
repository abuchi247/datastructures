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

def backspaceCompare(S: str, T: str) -> bool:
        s_iter = len(S) - 1
        s_main = -1
        
        t_iter = len(T) - 1
        t_main = -1
        
        s_found_hash = 0
        t_found_hash = 0
        
        while s_iter >= 0 or t_iter >= 0:
            if S[s_iter] == "#":
                s_found_hash +=1
                s_iter -= 1
                continue
            else:
                if s_found_hash > 0:
                    s_iter -= s_found_hash
                    s_found_hash = 0
                    continue
                else:
                    if s_iter >= 0:
                        s_main = s_iter
            if T[t_iter] == "#":
                t_found_hash += 1
                t_iter -= 1
                continue
            else:
                if t_found_hash > 0:
                    t_iter -= t_found_hash
                    t_found_hash = 0
                    continue
                else:
                    if t_iter >= 0:
                        t_main = t_iter        
                
            
            if S[s_main] != T[t_main]:
                return False
            
            s_iter -= 1
            t_iter -= 1
                       
        return True


if __name__ == "__main__":
  s = "ab#c"
  t = "ad#c"
  print(backspaceCompare(s, t))