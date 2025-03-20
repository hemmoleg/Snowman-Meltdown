from ascii_art import STAGES
import random
from snowman import WORDS

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def check_game_won(secret_word, guessed_letters):
    found_counter = 0
    for c in guessed_letters:
        if c in secret_word:
            found_counter += 1

    if found_counter == len(secret_word):
        return True
    else:
        return False


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.

    while mistakes < 4:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        guessed_letters.append(guess)
        if not guess in secret_word:
            mistakes += 1

        if check_game_won(secret_word, guessed_letters):
            print("GAME WON")
            exit()

    print("GAME OVER")

