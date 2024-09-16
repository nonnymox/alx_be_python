import random
play_again = "yes"  # Initialize the variable to enter the loop initially


while play_again == "yes":
    secret_number = random.randint(1, 10)
    print(secret_number)
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?\n"))
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

    play_again = input("Do you want to keep playing? (yes/no): ").strip().lower()
