# Import the random module
import random

# List of Christmas-themed words
christmas_words = ["snowman", "reindeer", "mistletoe", "elf", "gingerbread", "ho ho ho", "north pole", "santa claus"]

# Pick a random word from the list
word = random.choice(christmas_words)

# Create a list of underscores the same length as the word
guesses = ["_"] * len(word)

# Set the number of allowed guesses
num_guesses = 6

# Loop until the player has guessed all the letters or run out of guesses
while num_guesses > 0 and "_" in guesses:
    # Print the current state of the game
    print(" ".join(guesses))
    print(f"You have {num_guesses} guesses left.")
    
    # Get a guess from the player
    guess = input("Enter a letter: ")
    
    # Check if the guess is correct
    if guess in word:
        # If it is, update the list of guesses with the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                guesses[i] = guess
    else:
        # If it's not, subtract one from the number of allowed guesses
        num_guesses -= 1

# Print a message based on whether the player won or lost
if "_" in guesses:
    print("You lost! The word was:", word)
else:
    print("You won! The word was:", word)
