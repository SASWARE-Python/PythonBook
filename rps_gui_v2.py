# Python: Rock, Paper Scissors Game
# GUI version
# Program name: rps_gui_v2.py

# History
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 06.sep.2020 ars created and converted to GUI
# 06.sep.2020 ars re-organize code structure

from tkinter import *
from tkinter.ttk import *
import random


def gui():
    # default initial values
    rock = 1
    paper = 2
    scissors = 3

    # initial rules, they are dictionaries
    names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
    rules = {rock: scissors, paper: rock, scissors: paper}

    # initialize scores
    player_score = 0
    computer_score = 0

    rps_window = Toplevel()
    rps_window.title("Rock, Paper, Scissors")

    # the location of these variables could not be done at the best place within the code
    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_score = IntVar()
    computer_score = IntVar()

    player_choice.set(1)

    rps_frame = Frame(rps_window, padding='3 3 12 12', width=300)
    rps_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    rps_frame.columnconfigure(0, weight=1)
    rps_frame.rowconfigure(0, weight=1)

    Label(rps_frame, text="Player").grid(column=1, row=1, sticky=W)
    Radiobutton(rps_frame, text="Rock", variable=player_choice, value=1).grid(column=1, row=2, sticky=W)
    Radiobutton(rps_frame, text="Paper", variable=player_choice, value=2).grid(column=1, row=3, sticky=W)
    Radiobutton(rps_frame, text="Scissors", variable=player_choice, value=3).grid(column=1, row=4, sticky=W)

    Label(rps_frame, text="Computer").grid(column=3, row=1, sticky=W)
    Label(rps_frame, textvariable=computer_choice).grid(column=3, row=3, sticky=W)

    Button(rps_frame, text="Play", command=start).grid(column=2, row=2)

    Label(rps_frame, text="Score").grid(column=1, row=5, sticky=W)
    Label(rps_frame, textvariable=player_score).grid(column=1, row=6, sticky=W)

    Label(rps_frame, text="Score").grid(column=3, row=5, sticky=W)
    Label(rps_frame, textvariable=computer_score).grid(column=3, row=6, sticky=W)

    Label(rps_frame, textvariable=result_set).grid(column=2, row=7, sticky=W)

    # game main driver
    def start():
        print("Let's play a game of Rock, Paper, Scissors")
        while game():
            pass
        # scores()

    # game function
    def game():
        player = player_choice.get()
        computer = random.randint(1, 3)
        computer_choice.set(names[computer])

        result(player, computer)
        # return play_again()

    # player (e.g. user) types in its move, a number between 1 and 3
    # def move():
    #    while True:
    #        print
    #        player = input("Rock = 1\nPaper=2\nScissors=3\nMake a move: ")
    #        try:
    #            player = int(player)
    #            if player in (1, 2, 3):
    #                return player
    #        except ValueError:
    #            print("Oops: I didn't understand that. Please enter 1, 2 or 3.")

    def result(player, computer):
        new_score = 0
        # print("1 ...")
        # time.sleep(1)
        # print("2 ...")
        # time.sleep(1)
        # print("3!")
        # time.sleep(0.5)
        # print(f"Computer threw {names[computer]}")

        # global player_score, computer_score

        if player == computer:
            result_set.set("Tie game")
        else:
            if rules[player] == computer:
                result_set.set("Your victory has been assured")
                new_score = player_score.get()
                new_score += new_score
                player_score.set(new_score)
            else:
                result_set.set("The computer laughs as you realise you have been defeated.")
                new_score = computer_score.get()
                new_score += new_score
                computer_score.set(new_score)

    rps_window = Toplevel()
    rps_window.title("Rock, Paper, Scissors")

    # the location of these variables could not be done at the best place within the code
    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_score = IntVar()
    computer_score = IntVar()

    player_choice.set(1)

    rps_frame = Frame(rps_window, padding='3 3 12 12', width=300)
    rps_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    rps_frame.columnconfigure(0, weight=1)
    rps_frame.rowconfigure(0, weight=1)

    Label(rps_frame, text="Player").grid(column=1, row=1, sticky=W)
    Radiobutton(rps_frame, text="Rock", variable=player_choice, value=1).grid(column=1, row=2, sticky=W)
    Radiobutton(rps_frame, text="Paper", variable=player_choice, value=2).grid(column=1, row=3, sticky=W)
    Radiobutton(rps_frame, text="Scissors", variable=player_choice, value=3).grid(column=1, row=4, sticky=W)

    Label(rps_frame, text="Computer").grid(column=3, row=1, sticky=W)
    Label(rps_frame, textvariable=computer_choice).grid(column=3, row=3, sticky=W)

    Button(rps_frame, text="Play", command=start).grid(column=2, row=2)

    Label(rps_frame, text="Score").grid(column=1, row=5, sticky=W)
    Label(rps_frame, textvariable=player_score).grid(column=1, row=6, sticky=W)

    Label(rps_frame, text="Score").grid(column=3, row=5, sticky=W)
    Label(rps_frame, textvariable=computer_score).grid(column=3, row=6, sticky=W)

    Label(rps_frame, textvariable=result_set).grid(column=2, row=7, sticky=W)

+++

    # def play_again():
    #     answer = input("Would you like to play again? y/n: ").lower()
    #     if answer in ("y", "yes"):
    #         return answer
    #     else:
    #         print("Thank you very much for playing our game. See you next time!")

    # def scores():
    #     global player_score, computer_score
    #     print("HIGH SCORES")
    #     print(f"Player  : {player_score}")
    #     print(f"Computer: {computer_score}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
