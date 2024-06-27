import random

while True:
    print("WELCOME TO THE RANDOM NUMBER GENERATOR GAME! PLEASE CHOOSE AN INPUT BELOW")
    print("1. PLAY")
    print("2. EXIT")
    print("3. ABOUT")

    choice = input()

    if choice == "1":
        random_num = random.randint(1, 100)  # Generates a random number between 1 and 100
        attempts = 5  # Initialize the number of guesses
        print("YOU HAVE 5 GUESSES. THE NUMBER IS BETWEEN 1 AND 100")

        while attempts > 0:
            user_guess = int(input("ENTER A NUMBER: "))
            attempts -= 1  # Decrement the number of guesses after each attempt

            if user_guess < random_num:
                print("TOO LOW! TRY AGAIN")
            elif user_guess > random_num:
                print("TOO HIGH! TRY AGAIN")
            else:
                print("YOU GUESSED CORRECTLY! CONGRATULATIONS")
                break  # Exit the loop if the guess is correct

            if attempts == 0:
                print(f"CHANCES RAN OUT :/ YOU KINDA SUCK. THE CORRECT NUMBER WAS {random_num}")

    elif choice == "2":
        exit_choice = input("ARE YOU SURE? Y/N ")
        if exit_choice == "Y":
            print("EXITING...")
            break  # Exit the while loop to stop the game
        elif exit_choice == "N":
            print("RESTARTING GAME...")
        else:
            print("INVALID INPUT!")

    elif choice == "3":
        print("THIS IS A SIMPLE GUESSING GAME. YOU HAVE 51 ATTEMPTS TO GUESS THE NUMBER CORRECTLY.")

    else:
        print("INVALID INPUT!")
