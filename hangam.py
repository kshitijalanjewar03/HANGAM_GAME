import random

WORDS_AND_HINTS = [
    ("python", "A popular programming language."),
    ("giraffe", "Tallest animal on land."),
    ("keyboard", "An input device with keys."),
]

HANGMAN_PICS = [
    """
     ------
     |    |
     |
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
    _|_
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
    _|_
    """
]

def display_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word, hint = random.choice(WORDS_AND_HINTS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")

    while wrong_guesses < max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", display_progress(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess.")
            wrong_guesses += 1
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()