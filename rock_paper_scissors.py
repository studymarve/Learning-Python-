# Store all data needed for the game
import random

emojis = {
  "r" : "🌋", "p" : "📜", "s" : "✂️"
}
choices = ("r", "p", "s")
results = {
  ("r", "s"): "You win! Rock crushes Scissors!",
  ("s", "p"): "You win! Scissors cut Paper!",
  ("p", "r"): "You win! Paper covers Rock!",
  ("s", "r"): "You lose! Rock crushes Scissors!",
  ("p", "s"): "You lose! Scissors cut Paper!",
  ("r", "p"): "You lose! Paper covers Rock!"
}

# Ask users if they want to play
while True:
  user_choice = input("Do you want to play (y/n): ").lower().strip()
if user_choice in ("n" or "no"):
print("Goodbye 👋👋👋😘😘")
break
while True:

elif user_choice in ("y" or "yes"):
user_move = input("Rock, Paper, Scissors(r, p, s): ").lower().strip()
if user_move not in choices:
print("Invalid choice, press r for rock, p for paper, s for scissors")
else :
print("Please, Type only yes or no")
computer_move = random.choice(choices)
if user_move == computer_move:
print("It a Tie")
print(results[(user_move, computer_move)])
# Validate answers for errors(non words and number)

# Generate computer answers

# print result

# print the winner or loser

# Allow user to terminate the program