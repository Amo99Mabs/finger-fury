def main():
    print("Welcome to Finger Fury!")

if __name__ == "__main__":
    main()

import random

def get_user_choice():
    return input("Choose Rock, Paper, or Scissors: ").lower()

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "Its a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
        print("Welcome to Finger Fury!")
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"You chose {user}, computer chose {computer}")
        result = determine_winner(user, computer)
        print(result)


def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_input in choices:
            return user_input
        return("Invalid choice. Please try again.")
