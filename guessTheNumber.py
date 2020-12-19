import random
LOWER_LIMIT = 0
UPPER_LIMIT = random.randint(10, 20)
secretNumber = random.randint(LOWER_LIMIT, UPPER_LIMIT)
guesses = 10

while guesses > 0:
    try:
        guess = int(input("(Guesses left: %s) Enter an integer between %s and %s :" % (guesses, LOWER_LIMIT, UPPER_LIMIT)))
    except:
        continue #If user enters invalid input don't decrement their number of guesses
    if guess == secretNumber:
        print("You guessed the secret number")
        break
    else:
        guesses -= 1
        
if guesses == 0:
    print("Out of guesses!")
    
