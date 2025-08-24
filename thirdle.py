from letter_state import LetterState
from colorama import Fore, Style, Back
from typing import List
from random import randint


class Thirdle:

    WORD_LENGTH = 4  #Default word length
    MAX_ATTEMPTS = 6
    TOP_ROW = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    MIDDLE_ROW = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    BOTTOM_ROW = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

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
    
    def hint(self):
        if (self.MAX_ATTEMPTS - len(self.attempts)) < 3:
            print(Fore.RED + "\nTaking this hint would lose you the game, and you're no quitter!\n"
                  + Style.RESET_ALL)
        else:
            random_number = randint(0,self.WORD_LENGTH-1)
            random_character = self.secret[random_number]
            print(f"The character '{random_character}' can be found at positon {random_number + 1}")
            self.attempts.append(" ")
            self.attempts.append(" ")
            print(f"You have {self.remaining_attempts} attempts left.\n")
            return random_character

    def display_results(self, game):
        lines = []
        self.draw_top_boarder(lines)
        for word in game.attempts:
            if word == " ":
                print(Back.YELLOW + "    ┇ " + "_ " * self.WORD_LENGTH + "┇" + Style.RESET_ALL)
            else:
                result = game.guess(word)
                colored_result_str = self.convert_result_to_color(result,word)
                print("    ┇ " + colored_result_str + " ┇")
        for _ in range(self.remaining_attempts):
            print("    ┇ " + "_ " * self.WORD_LENGTH + "┇")
        self.draw_bottom_boarder(lines)
        
    def display_remaining_letters(self, userGuess):
        print(Fore.CYAN + "Remaining  letters:\n" + Style.RESET_ALL)
        userGuess = userGuess.lower()
        for x in range(0,len(self.TOP_ROW)):
            if self.TOP_ROW[x] in list(userGuess):
                self.TOP_ROW[x] = self.TOP_ROW[x].upper()
            if 91 > ord(self.TOP_ROW[x]) > 64:
                print(Fore.BLACK + self.TOP_ROW[x] + Style.RESET_ALL + " ", end = '')
            else:
                print(Fore.CYAN + self.TOP_ROW[x].upper() + " " + Style.RESET_ALL, end = '')
        print("\n")
        print(" ", end = '')
        
        for y in range(0,len(self.MIDDLE_ROW)):
            if self.MIDDLE_ROW[y] in list(userGuess):
                self.MIDDLE_ROW[y] = self.MIDDLE_ROW[y].upper()
            if 91 > ord(self.MIDDLE_ROW[y]) > 64:
                print(Fore.BLACK + self.MIDDLE_ROW[y] + Style.RESET_ALL + " ", end = '')
            else:
                print(Fore.CYAN + self.MIDDLE_ROW[y].upper() + " " + Style.RESET_ALL, end = '')
        print("\n")
        print("   ", end = '')
                
        for z in range(0,len(self.BOTTOM_ROW)):
            if self.BOTTOM_ROW[z] in list(userGuess):
                self.BOTTOM_ROW[z] = self.BOTTOM_ROW[z].upper()
            if 91 > ord(self.BOTTOM_ROW[z]) > 64:
                print(Fore.BLACK + self.BOTTOM_ROW[z] + Style.RESET_ALL + " ", end = '')
            else:
                print(Fore.CYAN + self.BOTTOM_ROW[z].upper() + " " + Style.RESET_ALL, end = '')
        print("\n")
        

    def convert_result_to_color(self, result: List[LetterState], word):
        result_with_color = []
        for letter in result:
            if letter.is_in_position:
                result_with_color.append(f"{Fore.GREEN}{letter.character}{Style.RESET_ALL}")
            elif letter.is_in_word:
                result_with_color.append(f"{Fore.MAGENTA}{letter.character}{Style.RESET_ALL}")
            else:
                result_with_color.append(f"{Fore.WHITE}{letter.character}{Style.RESET_ALL}")
        return " ".join(result_with_color)
    
    def draw_top_boarder(self, lines: List[str], pad: int = 1):
        content_length = self.WORD_LENGTH * 2 + 1
        top_boarder = "    ┏" + "┉" * content_length + "┓"
        print(top_boarder)

    def draw_bottom_boarder(self, lines: List[str], pad: int = 1):
        content_length = self.WORD_LENGTH * 2 + 1
        bottom_boarder = "    ┗" + "┉" * content_length + "┛"
        print(bottom_boarder + "\n")

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts [-1] == self.secret
    
    @property
    def remaining_attempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):

        return self.remaining_attempts > 0 and not self.is_solved
