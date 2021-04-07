import random

# Generating random number
secretNumber = random.randint(1, 100)

# Rules
print("The number is between 1 and 100.\nYou will get six chances to guess the number.")

# Mainloop
for guessesTaken in range(6):
    try:
        guessedNumber = int(input("Enter Your Number: "))
        if guessedNumber > secretNumber:
            print("Your guess is high.")
        elif guessedNumber < secretNumber:
            print("Your guess is low.")
        else:
            break
    except ValueError:
        print("You have to enter an integer.")

# Checking whether guessed number is right.
if guessedNumber == secretNumber:
    print(f"Good Job! You guessed the number in {guessesTaken} guesses.")
else:
    print(f"You guessed it wrong. The number was {secretNumber}")
