import random

# List of predefined words
words = ["python", "apple", "tiger", "school", "planet"]

# Randomly choose a word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display hidden word
hidden_word = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Final result
if "_" not in hidden_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)