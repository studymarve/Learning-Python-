while True:
    user_name = input("What is your name: ").strip().capitalize()
    
    if not user_name:
        print("Please type in your name (it can't be empty)")
        continue
        
    if not user_name.isalpha():
        print("Type only letters not number!")
        continue

    print(f"Hello {user_name}")
    print("This are four food, Which one is your favourite?")
    break
 
 
favourite_food = ["Rice" , "Beans", "Bread", "Pounded Yam"]
for index , food in enumerate(favourite_food, start = 1):
    print(f"{index}. {food}")
while True:
    raw_choice = input("Which food do you like most in 1-4? , Enter a number: ").strip()
    if not raw_choice:
        print("Please Type in yoir choice, it can't be empty")
        continue
    if not raw_choice.isdigit():
        print("Only numbers are allowed")
        continue
        choice = int(raw_choice)
    if 1<= choice <=4:
        selected_food = favourite_food[choice - 1]
        print(f"Nice choice for picking {selected_food}")    
        break
else:
    'Please enter a number between 1 to 4'