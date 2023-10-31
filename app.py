#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

def player_choice():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    transform = player_choice.lower()
    print("Player choice: " + player_choice)
    return player_choice

player_choice = player_choice()

#you can use the following code to get the computer's choice:
import random
def computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer choice: " + computer_choice)
    return computer_choice

computer_choice = computer_choice()

#you can use the following code to check if the player's choice is one of the three valid choices and if it's not, display a message on the console that says that the choice is invalid and ask the user to enter their choice again:
if player_choice in ["rock", "paper", "scissors"]:
   print("Valid choice")
   def game_rules():
    if player_choice == "rock" and computer_choice == "scissors":
        print("Player wins")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins")    
    elif player_choice == computer_choice:
        print("It's a tie, try again")
        player_choice
    else:
        print("Computer wins")
else:
    print("Invalid choice")

game_rules = game_rules()



#you can use the following code to ask the user if they want to play again:
play_again = input("Would you like to play again (yes/no): ")
if play_again == "yes":
    #calls the function to play again
    player_choice()
    computer_choice()
    game_rules()
    
else:
    print("Goodbye")