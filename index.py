def start_game():
    print("You are at a crossroads. Do you want to go left or right?")
    choice = input("> ").lower()

    if choice == "left":
        bear_room()
    elif choice == "right":
        treasure_room()
    else:
        print("Invalid choice. Try again.")
        start_game()

def bear_room():
    print("There is a giant bear here eating honey, you lose")
    # Add more choices here...

def treasure_room():
    print("You found the gold! You win!")

start_game()
