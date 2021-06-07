# Given a String of length S, reverse the whole string without reversing the individual
# words in it. Words are separated by dots.
#
# Input:
# The first line contains T denoting the number of testcases. T testcases follow. Each case contains a string S containing characters.
#
# Output:
# For each test case, in a new line, output a single line containing the reversed String.
#
# Constraints:
# 1 <= T <= 100
# 1 <= |S| <= 2000
#
# Example:
# Input:
# 2
# i.like.this.program.very.much
# pqr.mno
#
# Output:
# much.very.program.this.like.i
# mno.pqr


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def reverse_word(sentence):
    if len(sentence) == 0:
        return ""
    if len(sentence) == 1:
        return sentence

    words = sentence.split(".")
    start = 0
    end = len(words) - 1

    while start <= end:
        swap(words, start, end)
        start += 1
        end -= 1

    return ".".join(word for word in words)


def main():
    T = int(input())
    results = []
    while T > 0:
        sentence = input()
        results.append(reverse_word(sentence))
        T -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    # sentence = "i.like.this.program.very.much"
    # print(reverse_word(sentence))
    # sentence = "pqr.mno"
    # print(reverse_word(sentence))
    main()
