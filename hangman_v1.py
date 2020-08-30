# Linux: Hangman Game

from random import *

# initialize scores
player_score = 0
computer_score = 0


def hangedman(hangman):
    graphics = [
        """
              +--------+
              |
              |
              |
              |
              |
            ============
        """, """
              +--------+
              |        |
              |        O
              |
              |
              |
            ============
        """, """
              +--------+
              |        |
              |        O
              |       -|-
              |
              |
            ============
        """, """
              +--------+
              |        |
              |        O
              |       -|-
              |       / \
              |
            ============
        """]
    print(graphics[hangman])
    return


def start():
    print("Let's play Hangman")
    while game():
        pass
    scores()


def game():
    dictionary = ["gnu", "kernel", "linux", "mageia", "penguin", "ubuntu"]
    word = choice(dictionary)
    word_len = len(word)
    clue = word_len * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print(f"You already picked ({letter}")
            else:
                letters_tried += letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print(f"Sorry {letter} is not what we are looking for.")
                else:
                    print(f"Congratulations {letter} is correct")
                    for i in range(word_len):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Choose another")

        hangedman(letters_wrong)
        print(" ".join(clue))
        print(f"Guesses {letters_tried}")

        if letters_wrong == tries:
            print("Game over")
            print(f"The word was {word}")
            computer_score += 1
            break
        if "".join(clue) == word:
            print("You WON")
            print(f"The word was {word}")
            player_score += 1
            break
    return play_again()


def guess_letter():
    print(" ")
    letter = input("Take a guess at our mystery word: ")
    letter.strip()
    letter.lower()
    print(" ")
    return letter


def play_again():
    print(" ")
    answer = input("Would you like to play again? y/n: ").lower()
    if answer in ("y", "yes"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time.")


def scores():
    global computer_score, player_score
    print("HIGH SCORES")
    print(f"Player  : {player_score}")
    print(f"Computer: {computer_score}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
