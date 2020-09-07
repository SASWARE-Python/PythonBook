# Python: Rock, Paper Scissors Game

import random
import time

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


# game main driver
def start():
    print("Let's play a game of Rock, Paper, Scissors")
    while game():
        pass
    scores()


# game function
def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


# player (e.g. user) types in its move, a number between 1 and 3
def move():
    while True:
        print
        player = input("Rock = 1\nPaper=2\nScissors=3\nMake a move: ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            print("Oops: I didn't understand that. Please enter 1, 2 or 3.")


def result(player, computer):
    print("1 ...")
    time.sleep(1)
    print("2 ...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print(f"Computer threw {names[computer]}")

    global player_score, computer_score

    if player == computer:
        print("Tie game")
    else:
        if rules[player] == computer:
            print("Your victory has neen assured")
            player_score += 1
        else:
            print("The computer laughs as you realise you have been defeated.")
            computer_score += 1


def play_again():
    answer = input("Would you like to play again? y/n: ").lower()
    if answer in ("y", "yes"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print(f"Player  : {player_score}")
    print(f"Computer: {computer_score}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
