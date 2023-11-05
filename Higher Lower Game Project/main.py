#initial imports
from art import logo, vs
from game_data import data
from replit import clear
import random
#defining global variables
FINAL_SCORE = 0
RECORD_A = {}
RECORD_B = {}
user_input = ""
game_continue = True

#FUNCTION TO PICK UP A RECORD RANDOMLY
def select_record(data_list):
    """This function returns a random record from the provided data. The returned is a dictionary containing celebrity data."""
    return random.choice(data_list)

#INITIAL ASSIGNMENT FUNCTION FOR A AND B
def initial_assignment():
    """This function does the initial assignment for both compare A and compare B for the first time execution of the game. returns compare A         and compare B"""
    record_A = select_record(data)
    record_B = select_record(data)
    return record_A, record_B

#FUNCTION TO COMPARE AND MAINTAIN SCORE
def compare_records(record_1, record_2, input):
    """This function compares the follower count for both compare A and compare B as per the user provided input. It returns 2, if follower             count is same, returns '1' if user selected correct record and '0' if user selected wrong record."""
    follower_count_record_1 = record_1["follower_count"]
    follower_count_record_2 = record_2["follower_count"]
    if follower_count_record_1 == follower_count_record_2:
        return 2
    elif input == "A" and follower_count_record_1 > follower_count_record_2:
        return 1
    elif input == "B" and follower_count_record_2 > follower_count_record_1:
        return 1
    else:
        return 0

#function to reshuffle the records
def reshuffle_records(record_1, record_2):
    """This function assigns compare B to compare A and a new value to compare B for continuing the game."""
    record_1 = record_2
    record_2 = select_record(data)
    if record_1 == record_2:
        record_2 = select_record(data)
    return record_1, record_2

#function to print messages on the console.
def print_messages(record_A, record_B):
    """This function is to print the basic reptitive messages on to the console screen for every comparison."""
    clear()
    print(logo)
    if FINAL_SCORE != 0:
        print(f"You're right! Current score: {FINAL_SCORE}.")
    print(f"Compare A: {record_A['name']}, {record_A['description']}, from {record_A['country']}.")
    print(vs)
    print(f"Against B: {record_B['name']}, {record_B['description']}, from {record_B['country']}.")

def get_user_input_and_get_result():
    """This function is to get user input for comparison and then call compare_records() to compare records and accordingly maintain the
        final score and if the game should continue or not."""
    global FINAL_SCORE, RECORD_A, RECORD_B, game_continue
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    comparison_score = compare_records(record_1 = RECORD_A, record_2 = RECORD_B, input = user_input)
    if comparison_score == 1:
        FINAL_SCORE += 1
        RECORD_A, RECORD_B = reshuffle_records(record_1 = RECORD_A, record_2 = RECORD_B)
    elif comparison_score == 2:
        print("It's a draw, as both have same number of followers. You will not get any score for a draw.")
        RECORD_A, RECORD_B = reshuffle_records(record_1 = RECORD_A, record_2 = RECORD_B)
    else:
        game_continue = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {FINAL_SCORE}")
    
#This is a call to initial assignment function
RECORD_A, RECORD_B = initial_assignment()
#Below is a while loop to keep playing the game until user guesses wrong.
while game_continue:
    print_messages(record_A = RECORD_A, record_B = RECORD_B)
    get_user_input_and_get_result()
