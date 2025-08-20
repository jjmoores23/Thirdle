from letter_state import LetterState
from colorama import Fore, Style
from typing import List


class Thirdle:

    WORD_LENGTH = 4  #Default word length
    MAX_ATTEMPTS = 6

    def __init__(self, secret: str, word_size: int):
        self.secret: str =  secret.upper()
        self.attempts = []
        self.WORD_LENGTH = word_size
        pass

    def attempt(self, word: str):
        word = word.upper()
        if len(word) != self.WORD_LENGTH:
            print(Fore.RED
                  + f"Your word must be {self.WORD_LENGTH} characters long."
                  + Fore.RESET)
            return False
        else:
            self.attempts.append(word)
            if not self.is_solved and self.remaining_attempts > 0:
                print(f"Your guess '{word}' was incorrect. You have {self.remaining_attempts} attempts left.\n")
            return True
        
    def guess(self, word:str):
        word = word.upper()
        result = []

        for i in range(self.WORD_LENGTH):
            if len(word) != self.WORD_LENGTH:
                return "0"
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = self.secret[i] == character
            result.append(letter)

        return result
    
    def display_results(self, game):
        lines = []
        self.draw_top_boarder(lines)
        for word in game.attempts:
            result = game.guess(word)
            colored_result_str = self.convert_result_to_color(result)
            print("┇ " + colored_result_str + " ┇")
        for _ in range(self.remaining_attempts):
            print("┇ " + "_ " * self.WORD_LENGTH + "┇")
        self.draw_bottom_boarder(lines)

    def convert_result_to_color(self, result: List[LetterState]):
        result_with_color = []
        for letter in result:
            if letter.is_in_position:
                result_with_color.append(f"{Fore.GREEN}{letter.character}{Style.RESET_ALL}")
            elif letter.is_in_word:
                result_with_color.append(f"{Fore.YELLOW}{letter.character}{Style.RESET_ALL}")
            else:
                result_with_color.append(f"{Fore.WHITE}{letter.character}{Style.RESET_ALL}")
        return " ".join(result_with_color)
    
    def draw_top_boarder(self, lines: List[str], pad: int = 1):
        content_length = self.WORD_LENGTH * 2 + 1
        top_boarder = "┏" + "┉" * content_length + "┓"
        print(top_boarder)

    def draw_bottom_boarder(self, lines: List[str], pad: int = 1):
        content_length = self.WORD_LENGTH * 2 + 1
        bottom_boarder = "┗" + "┉" * content_length + "┛"
        print(bottom_boarder)

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts [-1] == self.secret
    
    @property
    def remaining_attempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):

        return self.remaining_attempts > 0 and not self.is_solved
