import random
def guess():
    rndNmbr = random.randint(0,100)
    numGuesses = 10
    counter = 0
    while(counter < numGuesses):
        guess = input("Guess a number:")
        if (int(guess) == rndNmbr):
            print("You Win!")
            break
        if (counter < numGuesses - 1):
            if (int(guess) > rndNmbr):
                    print("Lower")
            if (int(guess) < rndNmbr):
                    print("Higher")
            counter += 1
        else:
            print("You Lost!")
            break

guess()
