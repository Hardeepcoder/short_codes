import random

target = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number"))
    if guess == target:
        print("Cool, you are right number was ", target)
        exit
    elif (guess > target):
        print("Too High, Try again")
    else:
        print("Too Low, try again")
