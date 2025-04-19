import random
import time

correct_num = random.randint(1,10)
print(correct_num)
Guessing = False
GuessCount = 0

print("Please take a guess between 1 - 10")
print("-----------------------------------")
time.sleep(2)
while Guessing == False:
    Guess = input("what do you think the number might be : ")
    GuessCount += 1
    if int(correct_num) == int(Guess):
        print(f"You guessed the right number and it took {GuessCount} Guesses" )
        Guessing = True
        break
    else:
        print("Please try again")