import random

"""A simple Rock-Paper-Scissors game."""

# Game data
choices = ("r", "p", "s")
emojis = {"r": "🌋", "p": "📜", "s": "✂️"}
aliases = {
    'r': 'r',
     'rock': 'r',
    'p': 'p',
     'paper': 'p',
    's': 's',
     'scissors': 's'
}
winning_rules = {('r', 's'), ('s', 'p'), ('p', 'r')}

# Main game loop
def get_user_choice_on_playing():
    while True:
        mode = input("Do you want to play rock paper and scissors game (y/n): ").lower().strip()
    
        if mode in ('n', 'no'):
            print("Goodbye!")
            return False
        elif mode not in ("yes", "y"):
            print("Please enter yes or no.")
            continue
        else:
            return True
    
        # Inner game loop
def get_user_choice():
        while True:
            user_input = input("Rock, Paper or Scissors (r/p/s): ").lower().strip()
            user_choice = aliases.get(user_input)
            if user_choice not in choices:
                print("Invalid choice!.")
                continue
            else:
                return user_choice

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]} and the computer chose {emojis[computer_choice]}")

def determine_the_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            print("It's a tie!")
        else:
            result = (user_choice, computer_choice)
            if result in winning_rules:
                print("You win!")
            else:
                print("You lose!")
                
def play_game():                
    while True:
        if get_user_choice_on_playing():
            user_choice = get_user_choice()
            computer_choice = random.choice(choices)
            display_choices(user_choice, computer_choice)
            determine_the_winner(user_choice, computer_choice)
        
        
        # Ask if the user wants to play again
            should_continue = input("Do you want to play again (y/n): ").lower().strip()
            if should_continue in ('n', 'no'):
                print("Goodbye!")
                break  # Exit the loop if the user doesn't want to play again
        else:
            break  # Exit the loop if the user doesn't want to play initially
play_game()

