import random

# List of 5 predefined words
words = ["apple", "banana", "python", "school", "happy"]

# Randomly choose a word
secret_word = random.choice(words)

# Create blanks for the secret word
guessed_word = ["_"] * len(secret_word)

# Track guessed letters and remaining attempts
attempts_left = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while attempts_left > 0:
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # If guess is correct
    if guess in secret_word:
        print("Good job! Letter found.")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts_left -= 1
        print("Wrong guess! Attempts left:", attempts_left)

    print("Current word:", " ".join(guessed_word))

    # Check if player won
    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

# If player runs out of attempts
if attempts_left == 0:
    print("Game Over! The word was:", secret_word)
