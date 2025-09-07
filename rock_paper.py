import random

# Store game data
emojis = {"r": "🌋", "p": "📜", "s": "✂️"}
choices = ("r", "p", "s")
results = {
    ("r", "s"): "You win! Rock crushes Scissors!",
    ("s", "p"): "You win! Scissors cut Paper!",
    ("p", "r"): "You win! Paper covers Rock!",
    ("s", "r"): "You lose! Rock crushes Scissors!",
    ("p", "s"): "You lose! Scissors cut Paper!",
    ("r", "p"): "You lose! Paper covers Rock!"
}

while True:
    user_choice = input("Do you want to play (y/n): ").lower().strip()
