import random

def space_game():
    player_hunger = 0

    while True:
        print("\n====================")
        print("  Space Fish Hunter")
        print("====================")
        print("1. Eat Space Fish")
        print("2. Quit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            space_fish_size = random.randint(1, 10)
            print(f"You caught a space fish of size {space_fish_size}!")

            player_hunger += space_fish_size

            if player_hunger >= 20:
                print("You are full and won the game!")
                break
        elif choice == '2':
            print("Thanks for playing. You quit the game.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

        # Simulate time passing
        pla