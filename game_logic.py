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
    print()


def check_game_won(secret_word, guessed_letters):
    found_counter = 0
    for c in guessed_letters:
        if c in secret_word:
            found_counter += 1

    if found_counter == len(secret_word):
        return True
    else:
        return False


def get_play_again():
    while True:
        try:
            again = str(input("Play again? y/n: "))
            if again != 'y' and again != 'n':
                print("Please enter either 'n' or 'y'")
            else:
                break
        except ValueError:
            print("Please enter either 'n' or 'y'")

    return True if again == 'y' else False


def get_letter():
    while True:
        try:
            guess = str(input("Guess a letter: ")).lower()
            if len(guess) > 1:
                print("Please enter a single letter")
            else:
                return guess
        except ValueError:
            print("Please enter a single letter")


def play_game():
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0

        print("Welcome to Snowman Meltdown!")
        # For now, display the initial game state.
        while mistakes < 4:
            display_game_state(mistakes, secret_word, guessed_letters)

            guess = get_letter()
            print("You guessed:", guess)
            guessed_letters.append(guess)
            if not guess in secret_word:
                mistakes += 1

            if check_game_won(secret_word, guessed_letters):
                print("GAME WON")
                break

        if mistakes == 4:
            print("GAME OVER")

        if not get_play_again():
            exit()
        else:
            print()