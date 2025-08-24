from thirdle import Thirdle
from letter_state import LetterState
from colorama import Fore, Style
import random
from game_over import GameOver

def main():
    print("Hello Thirdle!\n")
    start = GameOver()
    print(start.welcome_screen())
    while True:
        word_size = str(input("Enter the word size for this game (3, 4, or 5): "))
        if word_size not in ['3', '4', '5']:
            print("Please enter a valid word size (3, 4, or 5).")
        else:
            word_set = load_word_set("data/wordle_words_" + word_size + ".txt")
            break
    secret = random.choice(list(word_set))
    game = Thirdle(secret, int(word_size))
    win_check = GameOver()

    print("\nIf a character is not in the word, the character will remain WHITE")
    print("\nIf a character is in the word but in the wrong location, \nit will become " + Fore.MAGENTA +
          "MAGENTA" + Style.RESET_ALL)
    print("\nIf a character is in the word AND is in the correct location, \nit will become "
          + Fore.GREEN + "GREEN" + Style.RESET_ALL)
    print("\nIf a hint has been used, the two effected guess-lines will \nbecome "
          + Fore.YELLOW + "YELLOW\n" + Style.RESET_ALL)
    
    while game.can_attempt:
        x = input("Enter your guess, or enter 'H' for a hint: ")
        if x.upper() == "H":
            y = input("This will use two of your guesses, are you sure you want help? (Y/N): ")
            if y.upper() == "Y":
                game.hint()
        else:
            game.attempt(x)
            result = game.guess(x)
            if result != "0":
                game.display_results(game)   
                game.display_remaining_letters(x) 
    if game.is_solved:
        print("You've won Thirdle!")
        print(win_check.result(True))
    else:
        print("You've run out of attempts. The word was:", game.secret)
        print(win_check.result(False))
    again = input("\n.\n\n.\n\n.\n...Care for another round of Thirdle? (Y/N): ")
    if again.upper() == 'Y':
        main()
    else:
        print("Until next time...")

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set
    
if __name__ == "__main__":
    main()
