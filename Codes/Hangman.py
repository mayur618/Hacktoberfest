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
