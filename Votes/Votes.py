# Votes.py
#
# Author: Omar Gabr
# This file tallies the votes from votes.txt according to the
# index of the candidate per line and assigns a varying score
# to calculate the total votes for each candidate

# open file
filename = open("votes.txt", "r")

# ask the user to enter the name of a candidate
candidate = input("Enter a candidate's name: ")

# intialize sum to store each candidate's score
score = 0

for line in filename:
    # split each line into different names
    names = line.split()
    # names becomes a list now
    # initialize discounting variable
    i = 0
    # check each name if same as user input
    for word in names:
        # score depends on index of selected candidate name
        if (candidate == word):
            score += 5 - i
        # incremenet discounting variable after each name search
        i += 1
# print overall score
print(f"{candidate}\'s score: {score}")

# close file
filename.close()
