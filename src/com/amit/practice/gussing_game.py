#!/usr/bin/python

import random

user_input = ''
num_guess = 0
new_guess = True
while True: 
    if new_guess == True:
        our_num = random.randint(1, 10)
        new_guess = False
    user_input = input("Guess a number between 1 and 9 (both inclusive) or type 'exit' to exit the game: ")
    if user_input == 'exit':
        print("You have taken " + str(num_guess) + " guessess");
        break;
    elif user_input is None or user_input == '':
        print("Input was blank or not a number, please input a number: ")
        continue;
    else:
        num_guess += 1
        user_num = int(user_input)
        if user_num == our_num:
            print("You have guessed correctly.")
            print("You have taken " + str(num_guess) + " gussess")
            num_guess = 0
            new_guess = True
        elif user_num < our_num:
            print("You have guessed too low!")
        else: 
            print("You have guessed too high!")

