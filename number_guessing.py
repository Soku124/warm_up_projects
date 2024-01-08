from random import randint


def game():
    number = randint(1, 11)
    while True:
        user = int(input("Enter number between 1 to 10: "))
        if user > number:
            print("Guessed number is greater than actual number!\n try Again!")
        elif user < number:
            print("Guessed number is less than actual number!\n try again!")
        else:
            print("Congo you won!")
            break


game()
