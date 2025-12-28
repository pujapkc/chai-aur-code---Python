from random import randint

game_level=input("Enter the level of game you want to play 1.Hard 2.Easy\n")

if game_level == "Hard":
    print("You will get 10 chances to guess the number")
    right_num = randint(0,100)
    for i in range(0,9):

        user_guess = int(input("Enter your guess \n"))

        if user_guess > right_num:
            print("Too high")
        elif user_guess< right_num:
            print("Too Low")
        else:
            print("correct guess")
elif game_level == "Easy":
     print("You will get 5 chances to guess the number")
     right_num = randint(0,100)
     for i in range(0,5):

        user_guess = int(input("Enter your guess\n"))

        if user_guess > right_num:
            print("Too high")
        elif user_guess< right_num:
            print("Too Low")
        else:
            print("correct guess")



