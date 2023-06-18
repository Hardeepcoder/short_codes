import random

def jumble():
    chances = 2
    words = ['kylie','gigi','kandel','bella']
    word = random.choice(words)

    jumble_word = ''.join(random.sample(word, len(word)))

    print(jumble_word)


    while True:
        if chances ==0:
            print("You lost")
            break
        guess = input("Guess the word")
        if guess != word:
            chances -=1
            print("Sorry its wrong", chances, "left")
        else:
            print("***Correct Guess***")
            break

jumble()
