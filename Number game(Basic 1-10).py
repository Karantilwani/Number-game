import random

result = random.randint(1, 10)
chances = 0

while chances < 3:
    print("Let's start the game\n")
    print("You have to enter a number between 1 to 10!", "Let's see if you guess what I am guessing")
    print("You'll get 3 Chances to guess!", "So Let's Begin")

    guess = int(input("Enter the number: "))

    if guess == result:
        print("You guessed it buddy!!")
    else:
        print("Oh!! You've lost\n")
        print("Wanna play again?")
        choice = input("Enter Yes or No\n")
        if choice == "Yes":
            pass
        if choice == "No":
            exit("Thanks for playing!!")
        else:
            while True:
                if choice.upper() == "YES":
                    break
                if choice.upper() == "NO":
                    exit("Thanks for playing!!")
                else:
                    print("Please enter valid choice(Yes or No)")
                    choice = input("Enter Yes or No\n")
                    continue
        chances += 1
if chances == 3:
    print("Ohh sorry! You've reached maximum number of chances!", "Correct answer is:", result, "\n", "Come back later!")
