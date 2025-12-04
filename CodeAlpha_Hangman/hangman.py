# Hangman Game - Python Project
# Made by Anu for CodeAlpha Python Internship

import random

# Words and their clues
words_with_clues = {
    "python": "A popular programming language.",
    "purple": "A colour you love.",
    "intern": "A trainee working to gain experience.",
    "bottle": "Used to store liquids.",
    "coffee": "A drink that keeps people awake.",
    "hangman": "The name of this game.",
    "algorithm": "A step-by-step method to solve a problem.",
    "portfolio": "A collection of investments, like stocks.",
    "strategy": "A careful plan to achieve a goal.",
    "variable": "A named storage location used in programming.",
}


def play_game():
    """Play one round of Hangman."""
    # Choose a random (word, clue) pair
    secret_word, clue = random.choice(list(words_with_clues.items()))

    lives = 7
    guessed_letters = []
    current_state = ["_"] * len(secret_word)

    # Reveal one random letter at the start (all its positions)
    revealed_index = random.randrange(len(secret_word))
    revealed_letter = secret_word[revealed_index]

    for index, letter in enumerate(secret_word):
        if letter == revealed_letter:
            current_state[index] = revealed_letter

    guessed_letters.append(revealed_letter)

    print("\nNew game started!")
    print("Clue:", clue)
    print("The word has", len(secret_word), "letters.")
    print("One letter is already revealed for you:", revealed_letter)
    print("Current word:", " ".join(current_state))
    print("You have", lives, "lives.\n")

    # Main guessing loop
    while lives > 0 and "_" in current_state:
        guess = input("Enter a letter: ").lower().strip()

        # Check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.\n")
            continue

        # Already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good job! The letter is in the word.")

            # Update current_state
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    current_state[index] = guess
        else:
            lives -= 1
            print("Wrong guess! You lost one life.")
            print("Lives left:", lives)

        print("Current word:", " ".join(current_state))
        print("Guessed letters:", ", ".join(guessed_letters))
        print("-" * 25)

    # After loop ends
    if "_" not in current_state:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nGame over! The word was:", secret_word)


def main():
    """Main menu for the Hangman game."""
    print("Welcome to Hangman!")
    print("1. Play")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice != "1":
        print("Okay, bye!")
        return

    # Play at least once, then ask to play again
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing! Game made by Anu for CodeAlpha internship.")
            break


if __name__ == "__main__":
    main()
