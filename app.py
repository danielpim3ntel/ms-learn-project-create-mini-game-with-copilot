#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

'''from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")'''

import random

valid_options = ['rock', 'paper', 'scissors']
outcomes = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}
player_score = 0
computer_score = 0

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in valid_options:
            return choice
        else:
            print("Invalid option. Please try again.")

def get_computer_choice():
    return random.choice(valid_options)

def determine_outcome(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif outcomes[player_choice] == computer_choice:
        return 'win'
    else:
        return 'lose'

def display_round_result(player_choice, computer_choice, outcome):
    print(f"You chose {player_choice}. The computer chose {computer_choice}. You {outcome}!")

def ask_play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid option. Please try again.")

while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    outcome = determine_outcome(player_choice, computer_choice)
    display_round_result(player_choice, computer_choice, outcome)
    if outcome == 'win':
        player_score += 1
    elif outcome == 'lose':
        computer_score += 1
    play_again = ask_play_again()
    if not play_again:
        break

print(f"Your final score is {player_score}.")
print(f"The computer's final score is {computer_score}.")
