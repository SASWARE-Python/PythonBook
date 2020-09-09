# Python Game: Hangman Game
# GUI version
# Program name: hangman_gui_v2.py

# History
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 08.sep.2020 ars created and converted to GUI
# 09.sep.2020 ars as with the Rock Paper Scissors game, its
#                 initial version from the Python Book did
#                 not work
#

from tkinter import *
from tkinter.ttk import *
from random import *

word = 0
word_length = 0
clue = 0
guess_count = 0


# initialize scores
# player_score = 0
# computer_score = 0

def gui():
    dictionary = ["gnu", "kernel", "linux", "mageia", "penguin", "ubuntu"]
    word = choice(dictionary)
    word_len = len(word)
    clue = word_len * ["_"]
    tries = 6
    guess_count = 0

    def hanged_man(hangman):
        graphic = [
            """
                            
                   
                   
                   
                   
                   
                ============
            """, """
                  |         
                  |
                  |
                  |
                  |
                  |
                ============
            """, """
                  +-----+
                  |
                  |
                  |
                  |
                  |
                ============
            """, """
                  +-----+
                  |        |
                  |        O
                  |
                  |
                  |
                ============
            """, """
                  +-----+
                  |        |
                  |        O
                  |       -|-
                  |
                  |
                ============
            """, """
                  +-----+
                  |        |
                  |        O
                  |       -|-
                  |       / \\
                  |
                ============
            """]
        graphic_set = graphic[hangman]
        hm_graphic.set(graphic_set)
        # return

    def game():
        global guess_count
        guess_count += 1

        print(f"Guesses {guess_count}")

        letters_wrong = incorrect_guesses.get()

        print(f"{letters_wrong}")

        print(f"{tries}")
        letter = guess_letter()
        first_index = word.find(letter)
        if first_index == -1:
            letters_wrong += 1
            incorrect_guesses.set(letters_wrong)
        else:
            for i in range(word_len):
                if letter == word[i]:
                    clue[i] = letter

        hanged_man(letters_wrong)
        clue_set = " ".join(clue)
        word_output.set(clue_set)

        if letters_wrong == tries or guess_count > tries:
            result_text = "Game Over. The world was {}".format(word)
            result_set.set(result_text)
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)
        if "".join(clue) == word:
            result_text = "You WON! The word was {}.".format(word)
            result_set.set(result_text)
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)

    def guess_letter():
        rt_letter = IntVar()
        letter = letter_guess.get()
        if len(letter) > 0:
            rt_letter.set(len(letter))
            print(f"{letter}; {len(letter)} -> {letter[len(letter) - 1:]}")
            letter = letter[len(letter) - 1:]
        letter.strip()
        letter.lower()
        Label(hm_frame, textvariable=rt_letter).grid(column=4, row=5)
        return letter

    def reset_game():
        global word, word_length, clue, guess_count
        incorrect_guesses.set(0)
        hanged_man(0)
        result_set.set("")
        letter_guess.set("")
        word = choice(dictionary)
        word_length = len(word)
        clue = word_length * ["_"]
        new_clue = " ".join(clue)
        word_output.set(new_clue)
        guess_count = 0

    # Top Level window
    hm_window = Toplevel()
    hm_window.title("Hangman")

    # variables
    incorrect_guesses = IntVar()
    incorrect_guesses.set(0)

    player_score = IntVar()
    computer_score = IntVar()

    result_set = StringVar()
    letter_guess = StringVar()
    word_output = StringVar()
    hm_graphic = StringVar()

    # game frame
    hm_frame = Frame(hm_window, padding="3 3 12 12", width=300)
    hm_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    hm_frame.columnconfigure(0, weight=1)
    hm_frame.rowconfigure(0, weight=1)

    Label(hm_frame, textvariable=hm_graphic).grid(column=2, row=1)
    Label(hm_frame, text="World").grid(column=2, row=2)
    Label(hm_frame, textvariable=word_output).grid(column=2, row=3)

    Label(hm_frame, text="Enter a letter").grid(column=2, row=4)
    Entry(hm_frame, exportselection=0, textvariable=letter_guess).grid(column=2, row=5)
    Button(hm_frame, text="Guess", command=game).grid(column=2, row=6)

    # Score Board
    Label(hm_frame, text="Wins").grid(column=1, row=7, sticky=W)
    Label(hm_frame, textvariable=player_score).grid(column=1, row=8, sticky=W)
    Label(hm_frame, text="Losses").grid(column=3, row=7, sticky=W)
    Label(hm_frame, textvariable=computer_score).grid(column=3, row=8, sticky=W)
    Label(hm_frame, textvariable=result_set).grid(column=2, row=9)
    Button(hm_frame, text="Reset", command=reset_game).grid(column=2, row=10)


# def play_again():
#     print(" ")
#     answer = input("Would you like to play again? y/n: ").lower()
#     if answer in ("y", "yes"):
#         return answer
#     else:
#         print("Thank you very much for playing our game. See you next time.")


# def scores():
#     global computer_score, player_score
#     print("HIGH SCORES")
#     print(f"Player  : {player_score}")
#     print(f"Computer: {computer_score}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()
