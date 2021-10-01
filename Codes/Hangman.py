import random

hang = ["""
H A N G M A N - Fruit Edition

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def getRandomWord():
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot',
             'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

    word = random.choice(words)
    return word

def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")
