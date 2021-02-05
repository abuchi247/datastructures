# Easy -> https://leetcode.com/problems/string-matching-in-an-array/

def stringMatching(words):
  # Time complexity: N*N
  # Space complexity: N
  result = set()

  for i in range(len(words)):
    for j in range(len(words)):
      if i != j:
        if words[i] in words[j]:
          result.add(words[i])
  return list(result)


if __name__ == "__main__":
  words = ["mass","as","hero","superhero"]
  print(stringMatching(words))