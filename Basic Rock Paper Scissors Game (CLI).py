import random

# Welcome text
print("ROCK PAPER SCISSORS")

# Game variables
ties = 0
wins = 0
losses = 0

# Gameloop
while True:
    # Displaying game data.
    print("%s Wins, %s Loses, %s Ties" % (wins, losses, ties))

    # Loop for player choice.
    while True:
        print("Enter any one: (r)ock (p)aper (s)cissor or (q)uit")
        player_move = input('- ').lower()
        if player_move == 'q':
            exit()
        elif player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print("Type one of: r, p, s or q")

    # Printing text according to choice.
    if player_move == 'r':
        print("ROCK versus...")
    elif player_move == 'p':
        print("PAPER versus...")
    elif player_move == 's':
        print("SCISSORS versus...")

    # Generating random number
    num = random.randint(1, 3)

    # Blank variable for computer move.
    computer_move = ''

    # Assigning values to computerMove accordingly.
    if num == 1:
        computer_move = 'r'
        print("ROCK")
    elif num == 2:
        computer_move = 'p'
        print("PAPER")
    elif num == 3:
        computer_move = 's'
        print("SCISSORS")

    # Condition for tie
    if player_move == computer_move:
        print("IT'S A TIE!")
        ties += 1

    # Conditions for wins
    elif player_move == 'r' and computer_move == 's':
        print("YOU WIN!")
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print("YOU WIN!")
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print("YOU WIN!")
        wins += 1

    # Conditions for losses
    elif computer_move == 'r' and player_move == 's':
        print("YOU LOSE!")
        losses += 1
    elif computer_move == 'p' and player_move == 'r':
        print("YOU LOSE!")
        losses += 1
    elif computer_move == 's' and player_move == 'p':
        print("YOU LOSE!")
        losses += 1
