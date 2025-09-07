from rock import get_user_choice, get_user_choice_on_playing, determine_the_winner, generate_computer_choice
while True:
    if get_user_choice_on_playing():
        user_choice = get_user_choice()
        computer_choice = generate_computer_choice()
        determine_the_winner(user_choice, computer_choice)

        should_continue = input("Do you want to play again (y/n): ").lower().strip()
        if should_continue in ('n', 'no'):
            print("Goodbye!")
            break
    else:
        break