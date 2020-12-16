import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("Enter the number between 1 and 100 \n"))
game_over = False

while game_over == False:
    if number == winning_number:
        print(f"You have guessed the right number in {guess} times")
        game_over = True

    elif number < winning_number:
            print("You have entered too low number\n")

    elif number > winning_number:
            print("You have entered too high number\n")

    else:
        print("Please input a positve integer")

    guess += 1
    number = int(input("Enter the number again \n"))
    
