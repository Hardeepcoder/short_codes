import random

def game():
    chicks = ["bella","gigi","kylie","kandle"]
    word = random.choice(chicks).lower()
    chances = 6
    guess_letters = []
    while True:
        display_word = ""

        for letter in word:
            if letter in guess_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        if "_ " not in display_word:
            print("*****Congrats, you have guess word******")
            break
        if chances ==0:
            print("You are lost")
            break

        guess = input("enter single letter")
        if guess.isalpha and len(guess) ==1:
            if guess in guess_letters:
                print("already guessed")
            elif guess in word:
                print("---Correct Guess----")
                guess_letters.append(guess)
            else:
                chances -=1
                print("Wrong guesss", chances,"Chances left")
        else:
            print("enter only single letter")
game()
