# my first "big" project in python. Trying to make 2 simple guessing games. One is a number guessing game and the other is a word guessing game.
# I will only be using basics (upto 2hours in bro codez python course) so only using if statements, for and while loops etc.
# this will have 4 parts. The main menu, the number guessing game, the word guessing game and a points system.
# for the main menu i will use a while true loop so the player can keep replaying as long as they want and quit whenever they want.
#starting main menu
total_points = 0
wins = 0
while True:
    print("Welcome to the arcade! Please select a game to play:")
    print("1. Number Guessing Game")
    print("2. Word Guessing Game")
    print("3. Quit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        # number guessing game code will go here
        print("welcome to the Number Guessing Game! Hope you are lucky enough to guess the number!")
        attempts = 3
        secret_number = 45 # for now as i dont know if i can even generate a random number so i'll just set it as my favourite number.
        for i in range(attempts):
            guess = int(input("Enter your guess. Upto 3 guesses allowed. It is a two-digit number: "))
            if guess == secret_number:
                print("Congratulations! You guessed the number!")
                wins += 1
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            break
        print(f"You won {wins} games!") # need to fix this so it keeps track of wins across multiple games, currently it resets to 0 every time the player chooses a game.
        total_points = wins * 10 
        print(f"Your total points: {total_points}")


         
    elif choice == "2":
        # word guessing game code will go here
        print("Welcome to the Word Guessing Game! Try to guess the secret word!")
        print("This game will be available soon!")
        pass
    elif choice == "3":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

print(f"You won {wins} games!")
total_points = wins * 10 
print(f"Your total points: {total_points}")