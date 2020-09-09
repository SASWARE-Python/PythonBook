# Python: Rock, Paper Scissors Game
# GUI version
# Program name: rps_gui_v3.py

# History
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 06.sep.2020 ars created and converted to GUI
# 06.sep.2020 ars re-organize code structure
# 06.sep.2020 ars ALL METHODS inside the windows frame must be declared first!

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
    # player_score = 0
    # computer_score = 0
    player_score = IntVar()
    computer_score = IntVar()
    draws = IntVar()
    games = IntVar()
    p_score_rate = DoubleVar()
    c_score_rate = DoubleVar()
    d_score_rate = DoubleVar()
    d_score_rate_str = StringVar()
    p_score_rate_str = StringVar()
    c_score_rate_str = StringVar()

    player_score.set(0)
    computer_score.set(0)
    draws.set(0)
    games.set(0)

    # game main driver
    def start():
        # print("Let's play a game of Rock, Paper, Scissors")
        while game():
            pass

    # game function
    def game():
        games.set(games.get() + 1)
        player = player_choice.get()
        computer = random.randint(1, 3)
        computer_choice.set(names[computer])
        result(player, computer)
        # return play_again()

    def result(player, computer):
        new_score = 0
        if player == computer:
            result_set.set("Tie game")
            draws.set(draws.get() + 1)
        else:
            if rules[player] == computer:
                result_set.set("Your victory has been assured")
                new_score = player_score.get()
                new_score += 1
                player_score.set(new_score)
            else:
                result_set.set("The computer laughs as you realise you have been defeated.")
                new_score = computer_score.get()
                new_score += 1
                computer_score.set(new_score)
        # update scores
        d_score_rate.set(draws.get() / games.get())
        p_score_rate.set(player_score.get() / games.get())
        c_score_rate.set(computer_score.get() / games.get())

        d_score_rate_str.set("{:.2f}%".format(100 * d_score_rate.get()))
        p_score_rate_str.set("{:.2f}%".format(100 * p_score_rate.get()))
        c_score_rate_str.set("{:.2f}%".format(100 * c_score_rate.get()))

    # main body of the windows/frame, it is better to place it at the bottom of the code
    rps_window = Toplevel()
    rps_window.title("Rock, Paper, Scissors")

    # the location of these variables could not be done at the best place within the code
    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    # player_score = IntVar()
    # computer_score = IntVar()

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
    Button(rps_frame, text="Exit", command=rps_window.destroy).grid(column=3, row=2)

    Label(rps_frame, text="GAMES").grid(column=2, row=5)
    Label(rps_frame, textvariable=games).grid(column=1, row=5, sticky=W)
    Label(rps_frame, textvariable=games).grid(column=3, row=5, sticky=W)

    Label(rps_frame, text="Score").grid(column=1, row=7, sticky=W)
    Label(rps_frame, textvariable=player_score).grid(column=1, row=8, sticky=W)

    Label(rps_frame, text="Draws").grid(column=2, row=7, sticky=W)
    Label(rps_frame, textvariable=draws).grid(column=2, row=8, sticky=W)

    Label(rps_frame, text="Score").grid(column=3, row=7, sticky=W)
    Label(rps_frame, textvariable=computer_score).grid(column=3, row=8, sticky=W)

    Label(rps_frame, textvariable=p_score_rate_str).grid(column=1, row=9, sticky=W)
    Label(rps_frame, textvariable=d_score_rate_str).grid(column=2, row=9, sticky=W)
    Label(rps_frame, textvariable=c_score_rate_str).grid(column=3, row=9, sticky=W)

    Label(rps_frame, textvariable=result_set, background='yellow').grid(column=2, row=10, sticky=W)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()
