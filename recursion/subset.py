def find_all_subsets(arr):
  subsets = []
  subsets.append([])
  for i in range(len(arr)):
    temp = []
    temp.append(arr[i])
    subsets.append(temp)
    for j in range(i+1, len(arr)):
      temp2 = temp  + [arr[j]]
      subsets.append(temp2)
  
  return subsets

if __name__ == "__main__":
  arr = [1, 2, 3, 4]
  print(find_all_subsets(arr))