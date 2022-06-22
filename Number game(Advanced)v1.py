import random

result = random.randint(1, 1000)
chances = 0

print("Let's start the game\n")
print("You have to enter a number between 1 to 1000!", "Let's see if you can guess the right answer")
print("You'll get 5 Chances to guess!", "When you'll go near to the correct one, you'll get hotter and vice-versa")

while chances < 5:

    guess = int(input("Enter the number: "))

    if guess == result:
        print("You guessed it buddy!!")
        break
    if 1 <= guess <= 200:
        print("It is cold!!", "Enter it again")
        pass
    if 201 <= guess <= 400:
        print("It is warm!!", "Enter it again")
        pass
    if 401 <= guess < result:
        print("It is Hot!!", "Enter it again")
        pass
    if result < guess <= 700:
        print("It is Hot!!", "Enter it again")
    if 701 <= guess <= 850:
        print("It is Warm!!", "Enter it again")
    if 851 <= guess <= 1000:
        print("It is Cold!!", "Enter it again")
    if guess > 1000:
        print("Sorry wrong input!!", "Please enter numbers between 1 and 1000")
    else:
        chances += 1

if chances == 5:
    print("Sorry you've reached maximum number of chances!!")
    exit("Thanks for playing!! Come back later!!")
