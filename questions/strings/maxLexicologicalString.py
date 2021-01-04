# https://leetcode.com/problems/last-substring-in-lexicographical-order/


def find_subsets(s):
  s_set = set()
  for i in range(len(s)):
      substring = s[i]
      s_set.add(substring)
      for j in range(i+1, len(s)):
          substring += s[j]
          s_set.add(substring)
  return s_set


if __name__ == "__main__":
  s = "abab"
  s = "leetcode"
  # print(max(find_subsets(s)))
  print(find_subsets(s))
                