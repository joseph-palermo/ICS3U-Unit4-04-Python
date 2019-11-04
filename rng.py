#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program checks if the guessed number is correct or not


import random


def main():
    # This function asks the user to guess the number

    # variables
    correct_number = random.randint(0, 9)

    # process
    while True:
        # input
        guess = input("Guess the number between 0 & 9 (integer): ")

        try:
            guess = int(guess)
            if guess == correct_number:
                print("")
                print("You correctly guessed the number!")
                break
            else:
                print("")
                print("Wrong number!")
                print("The correct number is: ", (correct_number))
                print("")
        except Exception:
            print("Please insert an integer.")


if __name__ == "__main__":
    main()
