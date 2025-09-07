import random

"""A simple Rock-Paper-Scissors game."""

choices = ("r", "p", "s",)
emojis = {"r" : "🌋", "p" : "📜", "s" : "✂️"}
normalised_choices = {
    'r': 'r',
    "rock": "r",
    'paper': "p",
    "p": "p",
    "scissors": "s",
    "s": "s"
}
winning_rules = {('r', 's'), ('s', 'p'), ('p', 'r')}

while True:
    mode = input("Do you want to play rock paper and scissors game (y/n): ").lower().strip()

    if mode in ('n', 'no'):
        print("Goodbye!")
        break
    if mode not in ("yes", "y"):
        print("Enter yes or no, Please")
        continue
    while True:
        
        user_choice = input("Rock, Paper and Scissors (r/p/s): ").lower().strip()
        if user_choice not in choices:
            user_choice = (normalised_choices[user_choice])
            
            break
        else:
            print("Invalid Choice, please pick one of: r, p, s")
            
    computer_choice = random.choice(choices)
    print(f"You choose {emojis[user_choice]} and computer choose {emojis[computer_choice]}")
   
    if user_choice == computer_choice:
        print("So it's a tie")
    else:
         result = (user_choice, computer_choice)
         if result in winning_rules:
             print("You win")
         else:
             print("You lost")
         print("More innovation coming soon")
      
         
   
            
    
        