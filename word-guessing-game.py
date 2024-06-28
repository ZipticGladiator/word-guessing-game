import random

#ask user for their username
print("What is your name?")
username = input()

print(f"Welcome to the word guessing game {username} . You have 12 turns to guess the word that has been randomly selected for you. Goodluck {username}!!!")

#create a list with random words assigned
wordlist = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam",
    "zucchini", "apricot", "blueberry", "cantaloupe", "dragonfruit", "elderflower",
    "feijoa", "guava", "huckleberry", "imbe", "jackfruit", "kumquat", "lime", "mulberry",
    "nashi", "olive", "persimmon", "quararibea", "rambutan", "sapote", "tamarind",
    "uva", "voavanga", "wolfberry", "ximenia", "yangmei", "ziziphus"
]

#a random word(r) must be selected from the list
r = random.choice(wordlist)
#ask user to select an alphabet(a)
#check if r contains a
#if r contains a,  show a and its correct index within r , else ask the user to guess another alphabet
#if the user has failed to answer the full word(r) within 12 guesses, terminate the program and return r