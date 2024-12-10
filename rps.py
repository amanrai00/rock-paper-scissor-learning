title = "Welcome to RPS"
print(title.center(36,"="))

import random
import sys
from enum import Enum


def rps(name='player one'):

    game_count = 0
    player_count = 0
    python_count = 0

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    def play_rps():

        nonlocal name
        nonlocal player_count
        nonlocal python_count

        player_choice = input(f"\n{name} Enter here:\n1 for ROCK \n2 for PAPER \n3 for SCISSOR\n\n")

        if player_choice not in ["1", "2", "3"]:
            print("Enter only 1, 2 or 3")
            return play_rps
        
        player = int(player_choice)

        computer = int(random.choice("123"))

        print(f"{name} chose {str(RPS(player)).replace("RPS.","")}.\n")
        print(f"Python chose {str(RPS(computer)).replace("RPS.","")}.\n")

        def game_solution(player,computer):
            
            nonlocal player_count
            nonlocal python_count

            if player == 1 and computer == 3:
                print(f"{name} Won🍾🍾")
                player_count += 1
            elif player == 2 and computer == 1:
                print(f"{name} Won🍾🍾")
                player_count += 1
            elif player == 3 and computer == 2:
                print(f"{name} Won🍾🍾")
                player_count += 1
            elif player == computer:
                print(f"Game Tie👌👌")
            else:
                print(f"Python Wins🐍🐍")
                python_count += 1
        
        result = game_solution(player,computer)
        print(result)

        nonlocal game_count

        game_count += 1

        print(f"\nTotal Game: {game_count}.")
        print(f"\n{name} Won: {player_count}.")
        print(f"\nPython Won: {python_count}.")

        while True:
            playagain = input(f"\n{name} Do you want to continue?\nY for yes N for no\n")

            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"Thank you for playing!")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!!")
            else:
                return
        
    return play_rps()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This is practise"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="Name of the person"
    )
    
    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)

    rock_paper_scissor()