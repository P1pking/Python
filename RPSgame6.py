import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0 
    player_wins = 0
    python_wins = 0 ###
    #syntax for constant data is in ALL CAPS

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        playerchoice = input(
            f"\n{name}, please enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n") # alt z

        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)


        #ctrl + d to highlight 2 indentical texts

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, you win!"
            elif player == computer:
                return "Tie Game"
            else:
                python_wins += 1
                return f"Python wins!\nSorry, {name}.. :("
            
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count # changed "global" to "nonlocal"
        game_count += 1
        # ctrl + d utilized
        print(f"\nGame count: {game_count}") 
        print(f"\n{name}'s wins: {player_wins}") 
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"\nGG\'s \nThank\'s for playing {name}! \n")
            sys.exit("As they in Russia... Paka Paka \n;)")
    return play_rps
# used shift+click to highlight text
# shift+tab to reverse tab




if __name__ == "__main__": # if statement allows to call function with out automatically running it
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to playing the game."
    )

    args = parser.parse_args()
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()