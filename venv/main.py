from random import *
def random_number():
    comp_number = randint(1,10)
    print(comp_number)
    return comp_number

def user_input(comp_number):
    user_guess = 0
    count = 1
    while user_guess!= comp_number:
        print("Guess #", count)
        user_guess = input("Type your number: ")
        if user_guess.isdigit():
            guesses(user_guess,comp_number,count)
            count +=1
        else:
            print("This is not a number! Start over!")
            user_input(comp_number)

def guesses(user_guess,comp_number,count):
    if int(user_guess) > comp_number:
        number_is_bigger()
    elif int(user_guess)<comp_number:
        number_is_smaller()
    else:
        number_is_equal(count)


def number_is_bigger():
    print("Your number is bigger!")

def number_is_smaller():
    print("Your number is smaller!")

def number_is_equal(count):
    print("You won from the", count, 'try!')
    exit(0)

user_input(random_number())

"""if user_guess>comp_number:
            print ("Your number is bigger!")
            count +=1
            continue
        elif user_guess<comp_number:
            print("Your number is smaller!")
            count +=1
            continue
        else:
            print("You won from the", count, 'try!')
            exit(0)"""


