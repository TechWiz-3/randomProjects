import random

real_number = random.randint(1,100)
guess_thresh = 4
current_guess = 0

while current_guess < guess_thresh:
    number_guess = int(input("Guess a number between 1-100: "))
    if real_number == number_guess:
        print("You guessed right")
        break
    else:
        print("You guessed wrong, try again")
    current_guess += 1