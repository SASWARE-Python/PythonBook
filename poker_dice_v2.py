# Python: poker_dice game version 2

import random
import time
from itertools import groupby


class BgColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    Reset = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Green = '\u001b[38;5;28m'
    Yellow = '\u001b[38;5;3m'
    Blue = '\u001b[38;5;4m'
    DarkBlue = '\u001b[38;5;21m'


# initialize rules
nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine: "9", ten: "10", jack: "J", queen: "Q", king: "K", ace: "A"}

player_score = 0
computer_score = 0
draws = 0

verbose = False

# who are you?
user_name = input("What is your name? ")
computer_hand = 0


def start():
    print(f"{BgColors.Blue}Welcome {user_name}, let's play a game of Linux's Poker Dice{BgColors.Reset}")
    while game():
        pass
    scores()


def game():
    global player_score, computer_score, draws
    print(f"{user_name}, the computer will help you throw the 5 dices")
    result = throw(False)
    user_hand = result[1]

    print(f"{BgColors.Blue}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{BgColors.Reset}")
    print(f"{BgColors.Blue}The Computer is playing now!{BgColors.Reset}")
    time.sleep(2)

    result = throw(True)
    if user_hand > result[1]:
        print(f"You won with a hand of {user_hand}")
        player_score += 1
    elif user_hand < result[1]:
        print(f"You lost, your hand is {user_hand}, computer hand {result[1]}")
        computer_score += 1
    else:
        print(f"It is a draw, a hand with a value of {user_hand}")
        draws += 1
    return play_again()


def throw(is_computer):
    user = user_name
    dice_to_roll_idx = 0
    if is_computer:
        user = f"{BgColors.Blue}Computer{BgColors.Reset}"

    roll_times = 5
    dice = roll(roll_times)

    result = show_hand(dice)
    print(f"{user}, you currently have '{result[0]}' with a value {result[1]}")

    if is_computer:
        print(f"{user} {BgColors.Yellow} is rolling {result[2]} dices {BgColors.Reset}")
        roll_times = result[2]
    else:
        roll_times = get_dices(user)
    if roll_times == 0:
        print(f"{user} You finish with {result[0]}")
    else:
        #    roll_times = dice_quantity
        dices_new_hand = roll(roll_times)
        dice_changes = list(range(roll_times))
        if verbose:
            print(f"Rolled {roll_times} dices")
            print(f"New dices {dice_changes}")
            print(f"Dices new {dices_new_hand}")

        print("Enter the number of a dice to re_roll? ")
        iterations = 0
        while iterations < roll_times:
            iterations += 1
            while True:
                if is_computer:
                    while True:
                        if dice.count(dice[dice_to_roll_idx]) == 1:
                            dice_to_roll_idx += 1
                            selection = dice_to_roll_idx
                            break
                        else:
                            dice_to_roll_idx += 1
                    print(f"Next dice? {BgColors.Green}{selection}{BgColors.Reset}")
                else:
                    selection = int(input("Next dice? "))
                try:
                    if selection in (1, 2, 3, 4, 5):
                        break
                except ValueError:
                    pass
                print("Oops! I didn't understand that. Please enter: 1, 2, 3, 4 or 5")
            dice_changes[iterations - 1] = selection - 1
            print(f"You have changed dice {selection} with {dice_changes[iterations - 1]}")

        print(f"After rolling {dice_changes}")
        iterations = 0
        while iterations < roll_times:
            iterations += 1
            replacement = dices_new_hand[iterations - 1]
            dice[dice_changes[iterations - 1]] = replacement

        result = show_hand(dice)
        print(f"{user}, You currently have '{result[0]}' with a value {result[1]}")
    return result


def get_dices(user):
    while True:
        try:
            dices = int(input(f"{user}, How many dices do you want to throw again? "))
            if dices in (0, 1, 2, 3, 4, 5):
                print(f"Dices {dices}")
                return dices
            else:
                print("Please enter: 0, 1, 2, 3, 4 or 5")

        except ValueError:
            print("Oops! I don't understand that. Please enter 0, 1, 2, 3, 4 or 5")
            pass


def roll(roll_number):
    numbers = range(1, 7)
    dice = list(range(roll_number))
    iterations = 0
    while iterations < roll_number:
        iterations += 1
        dice[iterations - 1] = random.choice(numbers)
    return dice


def show_hand(dice) -> object:
    hand_result = []

    # showing hand
    dice.sort()
    for d in range(len(dice)):
        print(f"Dice {d + 1} : {names[dice[d]]}")

    # hand result
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort()
    straight1 = [1, 2, 3, 4, 5]
    straight2 = [2, 3, 4, 5, 6]

    print(f"Dice Hand {dice_hand}")

    if dice == straight1 or dice == straight2:
        hand_result.append("a straight!")
        hand_result.append(5)  # hand value
        hand_result.append(0)  # new cards
        # return hand_result
    elif dice_hand[0] == 5:
        hand_result.append("five of a kind!")
        hand_result.append(8)  # hand value
        hand_result.append(0)  # new cards
        # return hand_result
    elif dice_hand[0] == 4:
        hand_result.append("four of a kind!")
        hand_result.append(7)
        hand_result.append(1)
        # return hand_result
    elif (dice_hand[0] == 3 and dice_hand[1] == 2) or (dice_hand[0] == 2 and dice_hand[1] == 3):
        hand_result.append("a full house!")
        hand_result.append(6)
        hand_result.append(0)
        # return hand_result
    elif (dice_hand[0] == 3 and dice_hand[1] == 1) or (dice_hand[0] == 1 and dice_hand[1] == 3) or (
            dice_hand[0] == 1 and dice_hand[1] == 1 and dice_hand[2] == 3):
        hand_result.append("three of a kind!")
        hand_result.append(4)
        hand_result.append(2)
        # return hand_result
    elif (dice_hand[0] == 2 and dice_hand[1] == 2) or (dice_hand[0] == 1 and dice_hand[1] == 2):
        hand_result.append("two pairs!")
        hand_result.append(3)
        hand_result.append(1)
        # return hand_result
    elif (dice_hand[0] == 2 and dice_hand[1] == 1 and dice_hand[2] == 1) or (
            dice_hand[0] == 1 and dice_hand[1] == 2 and dice_hand[2] == 1) or (
            dice_hand[0] == 1 and dice_hand[1] == 1 and dice_hand[2] == 1 and dice_hand[3] == 2):
        hand_result.append("one pair!")
        hand_result.append(2)
        hand_result.append(3)
        # return hand_result
    else:
        hand_result.append("a high card")
        hand_result.append(1)
        hand_result.append(4)
    return hand_result


def play_again():
    answer = input(f"{user_name}, Would you like to play again? y/n ").lower()
    if answer in ("y", "yes"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")


def scores():
    global player_score, computer_score, draws
    print("HIGH SCORES")
    print(f"Player  : {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws   : {draws}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
