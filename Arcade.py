# my first "big" project in python. Trying to make 2 simple guessing games. One is a number guessing game and the other is a word guessing game.
# I will only be using basics (upto 5.5 hours in bro codez python course) so only using if statements, for and while loops.Learnt about functions so added in functions to make the code more organized and easier to read.
# this will have 4 parts. The main menu, the number guessing game, the word guessing game and a points system.
# for the main menu i will use a while true loop so the player can keep replaying as long as they want and quit whenever they want.
#starting main menu
import random
total_points = 0
wins = 0
def number_guessing_game(wins,total_points):
    print("*************************************************")   
    print("welcome to the Number Guessing Game! Hope you are lucky enough to guess the number!")
    print("--------------------------------------------------")
    attempts = 5
    secret_number = random.randint(10,99)
    for i in range(attempts):
        try:
            guess = int(input("Enter your guess. Upto 5 guesses allowed. It is a two-digit number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            print("--------------------------------------------------")
            wins += 1
            break
        elif guess < secret_number:
            print("Too low! Try again.")
            print(f"You have {attempts - i - 1} guesses left.")
            print("--------------------------------------------------")
        else:
            print("Too high! Try again.")
            print(f"You have {attempts - i - 1} guesses left.")
            print("--------------------------------------------------")
        if i == attempts - 1:
            print(f"Sorry, you've used all your attempts! The secret number was: {secret_number}")  
            print("--------------------------------------------------")
    print(f"You won {wins} games!") 
    total_points = wins * 10 
    print(f"Your total points: {total_points}")
    print("*************************************************")
    return wins, total_points
def word_guessing_game(wins,total_points): 

        # word guessing game code will go here
    print("*************************************************")
    print("Welcome to the Word Guessing Game! Try to guess the secret word!")
    print("--------------------------------------------------")

    attempt = 5
    word_list = ["ninja", "kitty", "robot", "alien", "mages"]
    secret_word = random.choice(word_list)
    for i in range(attempt):
            guess = input("Enter your guess. Upto 5 guesses allowed: ")
            if guess.lower() == secret_word:
                print("Congratulations! You guessed the word!")
                print("--------------------------------------------------")
                wins += 1
                break
            else: 
                print("Wrong guess! Try again.")
                print(f"You have {attempt - i - 1} guesses left.")
                print("--------------------------------------------------")
                if i == 0:
                    print("Hint: The word starts with the letter " + secret_word[0])
                    print("--------------------------------------------------")
                elif i == 1:
                    print("Hint: The word has " + str(len(secret_word)) + " letters.")  
                    print("--------------------------------------------------")
                elif i == 2:
                    print("Hint: The word ends with the letter " + secret_word[-1])
                    print("--------------------------------------------------") 
                elif i == 3:
                    print("Hint: The word has the letter " + secret_word[1]) 
                    print("--------------------------------------------------")                   
                if i == attempt - 1:
                    print(f"Sorry, you've used all your attempts! The secret word was: {secret_word}") 
                    print("--------------------------------------------------")     
    print(f"You won {wins} games!")
    total_points = wins * 10 
    print(f"Your total points: {total_points}")    
    print("*************************************************")  
    return wins, total_points
while True:
    print("*************************************************")
    print("Welcome to the arcade! Please select a game to play:")
    print("1. Number Guessing Game")
    print("2. Word Guessing Game")
    print("3. Quit")
    print("*************************************************") 
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        wins, total_points = number_guessing_game(wins, total_points)
    elif choice == "2":
        wins, total_points = word_guessing_game(wins, total_points) 
    elif choice == "3":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please pick a valid option.")

print("*************************************************")
print(f"You won {wins} games!")
total_points = wins * 10 
print(f"Your total points: {total_points}")
print("*************************************************")