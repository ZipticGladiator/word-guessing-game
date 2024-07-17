import random

# Ask user for their username
print("What is your name?")
username = input()

print(f"Welcome to the word guessing game, {username}. You have 12 turns to guess the word that has been randomly selected for you. Good luck, {username}!!!")

# Create a list with random words assigned
wordlist = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam",
    "zucchini", "apricot", "blueberry", "cantaloupe", "dragonfruit", "elderflower",
    "feijoa", "guava", "huckleberry", "imbe", "jackfruit", "kumquat", "lime", "mulberry",
    "nashi", "olive", "persimmon", "quararibea", "rambutan", "sapote", "tamarind",
    "uva", "voavanga", "wolfberry", "ximenia", "yangmei", "ziziphus"
]

# A random word (r) must be selected from the list
r = random.choice(wordlist)
word_length = len(r)
guessed_word = ['_'] * word_length
turns = 12
guessed_letters = []

while turns > 0:
    print("Current word: " + " ".join(guessed_word))
    print(f"Turns left: {turns}")
    print("Guessed letters: " + ", ".join(guessed_letters))
    
    # Ask user to select an alphabet (a)
    print("Please select an alphabet:")
    alphabet = input().lower()
    
    # Ensure the user enters a single alphabetic character
    if len(alphabet) != 1 or not alphabet.isalpha():
        print("Invalid input. Please enter a single alphabet.")
        continue

    # Check if the letter was already guessed
    if alphabet in guessed_letters:
        print(f"You already guessed the letter '{alphabet}'. Try another one.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(alphabet)
    
    # Check if the selected alphabet is in the random word (r)
    if alphabet in r:
        print(f"Good guess! The letter '{alphabet}' is in the word.")
        for index, letter in enumerate(r):
            if letter == alphabet:
                guessed_word[index] = alphabet
    else:
        print(f"Sorry, the letter '{alphabet}' is not in the word.")
        turns -= 1

    # Check if the user has guessed the entire word
    if "_" not in guessed_word:
        print(f"Congratulations, {username}! You guessed the word '{r}' correctly!")
        break
else:
    print(f"Sorry, {username}. You've run out of turns. The word was '{r}'.")



'''
Explanation:
1. **User Input**: The user is prompted to enter their name.
2. **Word Selection**: A random word is selected from the list.
3. **Game Loop**: The game runs in a loop until the user either guesses the word or runs out of turns.
4. **Guessing**: The user is asked to guess a letter. The game checks if the letter is in the word and updates the display accordingly.
5. **End Game**: The game ends when the user guesses the word or runs out of turns, and the final result is displayed.
'''