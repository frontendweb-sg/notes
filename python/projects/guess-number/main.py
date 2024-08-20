from random import randrange


class GuessNumber:
    MAX_LIFE = 5
    guess_number = None
    level = 'easy'

    def __init__(self, life: int = 5) -> None:
        self.guess_number = randrange(1, 100)

    def set_level(self):
        """
        Prompts the user to choose a difficulty level.
        """
        while True:
            level = input(
                "Choose a difficulty level ('easy' or 'hard'): ").lower()
            if level in ['easy', 'hard']:
                self.level = level
                self.set_guess_number_range()
                break
            else:
                print("Invalid input. Please type 'easy' or 'hard'.")

    def choose_number(self):
        """
        Sets the range of the number to guess based on the chosen difficulty level.
        """
        if self.level == 'hard':
            self.level = 'hard'
            self.guess_number = randrange(1, 1000)
        else:
            self.level = 'easy'
            self.guess_number = randrange(1, 100)

    def init(self):
        count = 0
        exit = None
        level = self.type_level()
        self.choose_number(level)
        while True and self.life != count:
            try:
                num = int(input(f"Guess a number between {
                          '1 and 1000' if self.level == 'hard' else '1 and 100'}: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if num != self.guess_number:
                count += 1
                print(f"""Life:
                      {'#####'.rstrip('#'*count)}
                      """)
                print(f"""Incorrect number is {
                    num}, remaining life {self.life - count} or 'e' for exit""")
            else:
                print("You won!!, do you want to play again!")
                exit = input()
                if exit != 'e':
                    level = self.type_level()
                    self.choose_number(level)
                    count = 0
                    print(f"level: {self.level}")
            if exit == 'e':
                break
        else:
            print(f"You lost!! generated number was: {self.guess_number}")


if __name__ == "__main__":
    print("Welcome to the number Guessing Game!")
    # print("I'm thinking of a number between 1 and 100.")
    # print("Passt, the correct answer is 100")
    obj = GuessNumber()
    obj.init()
