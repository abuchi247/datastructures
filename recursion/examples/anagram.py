def findAnagram(string, result, anagramList):
  if len(string) == 0:
    anagramList.append(result)
    return

  for i in range(len(string)):
    ch = string[i]
    substring = string[:i] + string[i+1:]
    findAnagram(substring, ch + result, anagramList)


if __name__ == "__main__":
  anagramList = []
  findAnagram("abc", "", anagramList)
  print(anagramList)