import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You wake up in a mysterious land surrounded by dense fog.")
    time.sleep(1)
    print("You see two paths ahead: a 'forest' on the left and a 'cave' on the right.")

def choose_path():
    while True:
        # Get user input for path choice with error handling
        user_choice = input("Enter 'forest' or 'cave': ").lower()

        if user_choice in ['forest', 'cave']:
            return user_choice
        else:
            print("Invalid input. Please enter 'forest' or 'cave'.")

def explore_forest():
    print("You enter the dense forest.")
    time.sleep(1)
    print("As you wander deeper, you encounter a mystical creature.")
    time.sleep(1)
    print("Do you want to 'befriend' the creature or 'ignore' it?")

    user_choice = input("Enter 'befriend' or 'ignore': ").lower()

    if user_choice == 'befriend':
        # Positive outcome for befriending the creature
        print("The creature guides you to a magical spring, granting you special powers!")
    elif user_choice == 'ignore':
        # Neutral outcome for ignoring the creature
        print("The creature fades away, leaving you to explore the forest alone.")
    else:
        # Handle invalid input
        print("Invalid input. The creature looks at you strangely and vanishes.")

def explore_cave():
    print("You enter the dark cave.")
    time.sleep(1)
    print("Inside, you find a glowing gem and a menacing dragon.")
    time.sleep(1)
    print("Do you want to 'take' the gem or 'talk' to the dragon?")

    user_choice = input("Enter 'take' or 'talk': ").lower()

    if user_choice == 'take':
        # Player chooses to take the gem
        print("As you grab the gem, the dragon wakes up! You must 'fight' or 'run'.")

        user_choice = input("Enter 'fight' or 'run': ").lower()

        if user_choice == 'fight':
            # Positive outcome for fighting and defeating the dragon
            print("You defeat the dragon and secure the gem!")
        elif user_choice == 'run':
            # Neutral outcome for running away from the dragon
            print("You wisely run away, leaving the gem behind.")
        else:
            # Handle invalid input
            print("Invalid input. The dragon roars, unsure of your intentions.")
    elif user_choice == 'talk':
        # Player chooses to talk to the dragon
        print("You engage in a conversation with the dragon and learn about its lonely existence.")
        time.sleep(1)
        print("Do you want to 'befriend' the dragon or 'take' the gem?")

        user_choice = input("Enter 'befriend' or 'take': ").lower()

        if user_choice == 'befriend':
            # Positive outcome for befriending the dragon
            print("You befriend the dragon, and it becomes your loyal companion!")
        elif user_choice == 'take':
            # Player takes the gem after talking to the dragon
            print("As you take the gem, the dragon becomes enraged. You must 'fight' or 'apologize'.")

            user_choice = input("Enter 'fight' or 'apologize': ").lower()

            if user_choice == 'fight':
                # Neutral outcome for fighting the dragon after taking the gem
                print("You defeat the dragon, but the gem is tainted by the battle.")
            elif user_choice == 'apologize':
                # Positive outcome for apologizing to the dragon
                print("You apologize to the dragon, and it forgives you. The gem is now yours.")
            else:
                # Handle invalid input
                print("Invalid input. The dragon is confused and watches you leave.")
        else:
            # Handle invalid input
            print("Invalid input. The dragon looks at you skeptically.")

def main():
    introduction()
    path_choice = choose_path()

    if path_choice == 'forest':
        explore_forest()
    elif path_choice == 'cave':
        explore_cave()

if __name__ == "__main__":
    main()
