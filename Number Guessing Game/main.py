#let the computer select a random number between 1 and 100 everytime.
import random
number_selected = random.randint(1,100) #include 1 and 100

#import the logo from art.py file
from art import logo
#Welcome logo message.
print(logo)
print("Welcome to the number guessing game !!!")
print("I am thinking of a number between 1 and 100.")
print("Pssst, I have selected the number.")
#create a dictionary with difficulty level as key and number of attempts are value.
difficulty_level = {"easy": 10,
                    "hard" : 5,}
#ask the user to choose a difficulty level
user_selected_difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard'. ")
attempts = difficulty_level[user_selected_difficulty_level]

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > number_selected:
        print("Too high.")
    elif user_guess < number_selected:
        print("Too low.")
    else:
        print(f"You got it right. The answer was {number_selected}.")
        break
    attempts -= 1
    if attempts > 0:
        print("Guess again.")

if attempts == 0:
    print("You ran out of attempts. You lost !!!")
