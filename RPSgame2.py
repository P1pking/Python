import sys
import random
from enum import Enum

game_count = 0 ###
#syntax for constant data is in ALL CAPS
def play_rps():
  class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

  
  playerchoice = input("\nEnter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n") # alt z

  if playerchoice not in ["1","2","3"]:
    print("You must enter 1, 2, or 3.")
    return play_rps()

  player = int(playerchoice)
  

  #ctrl + d to highlight 2 indentical texts

  computerchoice = random.choice("123")

  computer = int(computerchoice)

  print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
  print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

  def decide_winner(player, computer):
    if player == 1 and computer == 3:
        return "You win!"
    elif player == 2 and computer == 1:
        return "You win!"
    elif player == 3 and computer == 2:
        return "You win!"
    elif player == computer:
        return "Tie Game"
    else:
        return("Python wins!")
    
  game_result = decide_winner(player, computer)

  print(game_result)

  global game_count
  game_count += 1

  print("\nGame count: " + str(game_count))

  print("\nPlay again?")

  while True:
    playagain = input("\nY for Yes or \nQ to Quit\n")
    if playagain.lower() not in ["y","q"]:
      continue
    else:
      break

  if playagain.lower() == "y":
    return play_rps()
  else:
    print("\nGG\'s \nThank\'s for playing! \n")
    sys.exit("As they in Russia... Paka Paka \n;)")
# used shift+click to highlight text
# shift+tab to reverse tab


play_rps()