
import random

# List of words for the game
WORDS = [
    "python", "computer", "hangman", "developer",
    "program", "network", "science", "keyboard"
]

MAX_ATTEMPTS = 6

# ASCII gallows stages: 0 to 6 incorrect guesses
HANGMAN = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("\n=== WELCOME TO HANGMAN ===")
    print("Guess the hidden word one letter at a time!")
    print("You have 6 incorrect guesses available.\n")

    while attempts_left > 0:
        # Display the current gallows
        mistakes = MAX_ATTEMPTS - attempts_left
        print(HANGMAN[mistakes])

        # Display correctly guessed letters and blanks
        display_word = " ".join(
            letter.upper() if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("Word:", display_word)

        print("Guessed letters:", " ".join(
            sorted(guessed_letters | wrong_letters)
        ) or "None")

        print("Attempts left:", attempts_left)

        # Check whether the player has won
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:",
                  secret_word.upper())
            print("You won the game!")
            return

        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).\n")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter. Try another!\n")
            continue

        # Process the guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!\n")
        else:
            wrong_letters.add(guess)
            attempts_left -= 1
            print("Incorrect guess!\n")

    # Game over
    print(HANGMAN[MAX_ATTEMPTS])
    print("Word:", " ".join(secret_word.upper()))
    print("\nGame over! You ran out of attempts.")
    print("The secret word was:", secret_word.upper())


if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing Hangman!")
            break
        print()
