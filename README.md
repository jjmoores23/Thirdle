# Thirdle
Terminal-based version of the popular game "Wordle", with options to solve a puzzle of three, four, or five characters in length.

# **How To Run**
Thirdle is ran inside of your computers terminal via Python.

If python is not downloaded on your computer, it can be downloaded here:

    https://www.python.org/downloads/macos/

To have colours present in the game, the following must be ran in terminal:

    pip install colorama

Then, navigate your terminal to access the download location of the games files
(Through a series of "cd"'s and "ls"'s)

Once inside of the file, run

**Windows**

    python play_thirdle.py

**MacOS**

    python3 play_thirdle.py

# **How To Play**
First, select the length of word you would like to solve for (3/4/5)

Once selected, you can type your first guess into the terminal and press enter to submit your guess

Letters not in the word will be **White**

Letters in the word but placed incorrectly will be **Yellow**

Letters in the word AND placed correctly will be **Green**

The user has six attempts to guess the word. It's made clear when a win/ loss condition has been met.

When the game is over, the code will stop running, and to play again. the user simply needs to run the game again.

# **NOTES**

This game was made in a day for fun, and as a refresher of python skills, a very simple piece of coding.

I hope you enjoy!
