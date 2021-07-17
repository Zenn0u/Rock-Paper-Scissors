import random

def play():
    while True:
        user = input("'r' for rock, 'p' for paper, 's' for scissors, 'q' to quit\n")
        computer = random.choice(['r','p','s'])

        if user == 'q':
            print("Game Over!")
            return

        print(is_win(user, computer))

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p'and computer == 'r') or \
        (user == 's' and computer == 'p'):
        return "You Won!\n"

    elif user == computer:
        return "It's a tie!\n"

    else:
        return "You Lost!\n"

play()