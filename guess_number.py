title = "Welcome to guess my number"
print(title.center(36,"="))

import random
import sys

def play(name='player one'):

    game_count = 0
    player_wins = 0

    def guess_play():

        nonlocal name

        player_choice = input(f"hey {name} Guess the number and enter below:\n")

        if player_choice not in ["1","2","3"]:
            print(f"Enter only 1, 2 or 3.")
            return guess_play
        
        player = int(player_choice)

        computer = int(random.choice("123"))

        print(f"You chose {player}\n")

        def game_result(player, computer):
            nonlocal player_wins
            if player == computer:
                print(f"{name} Guessed the right number🍾🍾\n")
                player_wins += 1
            else:
                print(f"{name} Sorry Wrong number👎👎\n")
        
        result = game_result(player,computer)
        print(result)

        nonlocal game_count

        game_count += 1

        print(f"Total game: {game_count}\n")
        print(f"{name} win {player_wins/game_count:.2%}.\n")

        while True:
            playagain = input(f"{name}Do you want to continue?\nY for yes Q for quit\n")

            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return guess_play()
        else:
            print(f"Thank you for playing!")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!!")
            else:
                return

    return guess_play()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This is the guess number module."
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="Enter name here"
    )

    args = parser.parse_args()

    guess_the_number = play(args.name)

    guess_the_number()