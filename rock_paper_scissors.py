import random


def play():

    computer = random.choice(['r', 'p', 's'])
    print(computer)
    user = input(
        "Choose a option: \n'r' for rock\n'p' for paper\n's' for scissors\n")

    print(winner(user, computer))


def winner(user, opponent):
    if (user == opponent):
        return 'It\'s a tie'

    if ((user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r')):
        return 'You Win!'

    return "You lost!"


if __name__ == "__main__":
    play()
