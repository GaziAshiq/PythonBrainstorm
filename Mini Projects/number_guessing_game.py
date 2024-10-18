from random import randint


class NumberGuess:
    """
        Represent a number guessing game.

        Attributes:
            min_number (int): The minimum number for the guessing range.
            max_number (int): The maximum number for the guessing range.
            turn (int): The number of turns allowed for guessing.
            number_to_guess (int): The randomly generated number to be guessed.
        """

    def __init__(self, min_number: int, max_number: int, turn: int) -> None:
        self.min_number = min_number
        self.max_number = max_number
        self.turn = turn
        self.number_to_guess = randint(min_number, max_number)

    def guess(self, guess_number: int) -> str:
        if self.turn > 0:
            if guess_number == self.number_to_guess:
                return 'Congratulations! You guessed the number.'
            elif guess_number > self.number_to_guess:
                self.turn -= 1
                return 'Try a smaller number.'
            else:
                self.turn -= 1
                return 'Try a larger number.'
        return f'You lost! The number was {self.number_to_guess}.'


print('Welcome to the Number Guessing Game!')
try:
    min_num = int(input('Enter the minimum number: '))
    max_num = int(input('Enter the maximum number: '))
    turns = int(input('Enter the number of turns: '))
    game = NumberGuess(min_num, max_num, turns)

    while game.turn > 0:
        guess_number = int(input('Enter your guess: '))
        result = game.guess(guess_number)
        print(result)
        if 'Congratulations' in result or 'You lost' in result:
            break
except ValueError as e:
    print(f'Please Enter valid number. !Error: {e}')
