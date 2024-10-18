import random

class HangManGame:
    DEFAULT_LIVES = 6

    def __init__(self):
        self.chosen_word: bool = False
        self.guessed_letters: set = set()
        self.is_completed: bool = False
        self.__word: str = ""
        self.lives = HangManGame.DEFAULT_LIVES

    def random_word(self):
        with open("wordlist.txt", "r") as fp:
            words = fp.read().splitlines()
            word_index = random.randint(0, len(words) - 1)
        self.set_chosen_word(words[word_index])

    def set_chosen_word(self, word: str):
        self.__word = word.strip().lower()
        self.chosen_word = True

    def draw_board(self):
        board = self.draw_hangman() + "\n"

        for letter in self.__word:
            if letter == " ":
                board += "  "
            elif letter in self.guessed_letters:
                upper_letter = letter.upper()
                board += upper_letter + " "
            else:
                board += "_ "

        board += f"\nLives remaining: {self.lives}"

        print(board)

    def draw_hangman(self):
        stages = [
            """
                -----
                |   |
                O   |
                /|\\  |
                / \\  |
                    |
            ---------
            """,
            """
                -----
                |   |
                O   |
                /|\\  |
                /    |
                    |
            ---------
            """,
            """
                -----
                |   |
                O   |
                /|\\  |
                    |
                    |
            ---------
            """,
            """
                -----
                |   |
                O   |
                /|   |
                    |
                    |
            ---------
            """,
            """
                -----
                |   |
                O   |
                |   |
                    |
                    |
            ---------
            """,
            """
                -----
                |   |
                O   |
                    |
                    |
                    |
            ---------
            """,
            """
                -----
                |   |
                    |
                    |
                    |
                    |
            ---------
            """
        ]
        return stages[self.lives]

    def validate_winning(self):
        for letter in self.__word.replace(" ", ""):
            if letter not in self.guessed_letters:
                return False

        return True

    def make_guess(self, letter: str):
        if len(letter) != 1:
            print("Please enter a single letter")
            return

        if letter in self.guessed_letters:
            print("You've already guessed this letter")
            return

        self.guessed_letters.add(letter)

        if letter not in self.__word:
            self.lives -= 1

    def play(self):
        while not self.is_completed:
            self.draw_board()
            self.make_guess(input("Enter a letter: "))

            if self.lives <= 0:
                self.draw_board()
                print("You've lost!")
                self.is_completed = True
            elif self.validate_winning():
                self.draw_board()
                print("You've won!")
                self.is_completed = True


if __name__ == "__main__":
    game = HangManGame()
    game.random_word()
    game.play()