# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is **z**."
#
# e.g.
#
# name1 = "Angela Yu"
#
# name2 = "Jack Bauer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."

def calculate_love(name1, name2):
    string1 = "TRUE".lower()
    string2 = "LOVE".lower()

    combined_names = (name1 + name2).lower()

    true_total = 0

    for s in string1:
        count = 0
        for i in combined_names:
            if s == i:
                count +=1
        true_total += count

    love_total = 0
    for s in string2:
        count = 0
        for i in combined_names:
            if s == i:
                count +=1
        love_total += count

    print(str(true_total * 10 + love_total) + "%")



if __name__ == "__main__":
    name1 = "Abuchi Kenneth Obiegbu"
    name2 = "Ayomide Fatimat Olatunbosun"

    name1 = "Abuchi Kenneth Obiegbu"
    name2 = "Onyedika Cecelia Eneh"

    calculate_love(name1, name2)