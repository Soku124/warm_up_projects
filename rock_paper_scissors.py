from random import randint


def game():
    com = randint(0, 2) # computer choices

    user = int(input("0 for rock\n1 for paper\n2 for scissors: ")) # user choice
    print("\n\t Computer choose: ", com) # showing computer choice to user

    if com == user:
        print("Game Draw!")
    elif (com == 0 and user == 1) or (com == 1 and user == 2):
        print("You won!")
    elif (com == 1 and user == 0) or (com == 2 and user == 1):
        print("Computer won!")
    elif (com == 1 and user == 2) or (com == 2 and user == 0):
        print("You won!")
    else:
        print("Computer won!")


def run_game():
    while True:
        game()

        again = input("press Y to play again else N: ")
        if again.lower() == "n":
            print("\n\n\t\t Thanks for playing.")
            break


run_game()
