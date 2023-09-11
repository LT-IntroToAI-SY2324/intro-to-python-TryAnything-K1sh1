# We will write a rock paper scissors game in class - Complete it in this file

#getting all the function from the random file

from inspect import getcallargs
import random

#creating place holder function for the player choice

playerChoice = input("choose between rock,paper, and scissors: ") # gets input of the user choice between rock paper and scissors

# function that gives the computer the options it can choose betwen rock paper ans scissors
# names a variable called player that ets the players answer choice between rock paper and scissors
# makes the computer choose a random option betwenn for paper and scissors

def getChoice():
    options = ["rock","paper","scissors"]
    player = playerChoice
    computerChoice = random.choice(options)
    chosen = {"player": player, "computer": computerChoice}
    return chosen

def winner(player,computer):
    print(f"you choose {player} and the computer choose {computer}")
    if player == computer:
        print("tie")
    elif player == "rock" and computer == "scissors":
        print("rock beats scissors you win")
    elif player == "rock" and computer == "paper":
        print(" paper beats rock you loose")
    elif player == "scissors" and computer == "rock":
        print("rock beats scissors you loose")
    elif player == "scissors" and computer == "paper":
        print("scissors beats paper you win")
    elif player == "paper" and computer == "rock":
        print("paper beats rock you win")
    elif player == "paper" and computer == "scissors":
        print("scissors beats paper you loose")

choices = getChoice()
result = winner(choices["player"], choices["computer"])
print(result)


