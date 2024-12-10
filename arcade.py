import sys
from rps import rps
from guess_number import play

def play_game(name='player one'):
    welcome_back = False

    while True:
        
        if welcome_back == True:
            print(f"\n{name}Welcome back to Arcade")
        
        player_choice = input(f"Please choose a game \n1 for rock, paper and scissor \n2 for guess number \nX for exit")

        if player_choice not in ["1","2","x"]:
            print(f"\nPlease enter only 1, 2 or x")
            return play_game()
        
        welcome_back = True

        if player_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
            guess_the_number = play(name)
            guess_the_number()
        else:
            print(f"Thank you for playing {name}!!")
            sys.exit()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Enter the name here"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="Enter the name here"
    )

    args = parser.parse_args()

    print(f"\nWelocme {args.name} to the Arcade🐲🐲")

    play_game(args.name)