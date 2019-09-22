from random import *

def random_number():
    global comp_number
    comp_number = randint(1,10)
    #print(comp_number)
    return comp_number

def user_input():
    user_guess = 0
    global count
    count = 1
    random_number()
    while user_guess!= comp_number:
        print("Guess #", count)
        user_guess = input("Type your number: ")
        if user_guess.isdigit():
            guesses(user_guess)
            count+=1
        else:
            print("This is not a number! Try again!")
            count+=1
            pass

def guesses(user_guess):
    if int(user_guess) > comp_number:
        number_is_bigger()
    elif int(user_guess)<comp_number:
        number_is_smaller()
    else:
        number_is_equal()


def number_is_bigger():
    print("Your number is bigger!")

def number_is_smaller():
    print("Your number is smaller!")

def number_is_equal():
    print("You won from the", count, 'try!')
    exit(0)

if __name__ == '__main__':
    user_input()
else:
    print("imported")



