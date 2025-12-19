import random

# ASCII art for hangman stages
HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]


def load_words(filename):
    """Загружает слова из файла."""
    with open(filename, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
    return words


def choose_word(words):
    """Выбирает случайное слово из списка."""
    return random.choice(words)


def display_word(word, guessed_letters):
    """Отображает слово с угаданными буквами."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def get_guess(guessed_letters):
    """Получает букву от пользователя."""
    while True:
        guess = input("Угадайте букву: ").lower()
        if len(guess) != 1:
            print("Пожалуйста, введите одну букву.")
        elif guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
        elif not guess.isalpha():
            print("Пожалуйста, введите букву.")
        else:
            return guess


def play_hangman():
    """Основная функция игры."""
    words = load_words("words.txt")
    word = choose_word(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("Добро пожаловать в игру 'Виселица'!")
    print("У вас есть 6 попыток, чтобы угадать слово.")
    print(display_word(word, guessed_letters))

    while wrong_guesses < max_wrong:
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Верно! Буква '{guess}' есть в слове.")
        else:
            wrong_guesses += 1
            print(
                f"Неверно! Буквы '{guess}' нет в слове. Осталось попыток: {max_wrong - wrong_guesses}"
            )

        print(HANGMAN_STAGES[wrong_guesses])
        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Поздравляем! Вы угадали слово!")
            return

    print(f"Вы проиграли! Слово было: {word}")


if __name__ == "__main__":
    play_hangman()
