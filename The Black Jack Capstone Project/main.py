import random
from art import logo
from replit import clear
#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """This function returns a random card from the list of cards."""
    return random.choice(cards)

#Hint: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. Look up the sum() function to help you do this.
#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
def calculate_score(card_list):
    """This function returns the score for the cards based on the black jack game rules."""
    if len(card_list) == 2 and 11 in card_list and 10 in card_list:
        return 0 
    the_score = sum(card_list)
    if the_score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        the_score = sum(card_list)
    return the_score

#Hint: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(score_of_user, score_of_computer):
    """This function compares the scores for user and computer and then prints the winner of the game."""
    if score_of_computer == 0:
        print("Its a Blackjack for computer. Computer wins !! You loose.")
    elif score_of_user == 0:
        print("Yaaay, Its a BlackJack for you, You win !!")
    elif score_of_computer == score_of_user:
        print("It's a Push. Your score and computer score are equal, it's a draw. ")
    elif score_of_user > 21:
        print("Its a Bust. Your score went over 21, You loose !!")
    elif score_of_computer > 21:
        print("Its a win for you and a bust for computer. You win, computer looses !!")
    else:
        if score_of_user > score_of_computer:
            print("Yaaay, you win !!")
        else:
            print("Computer wins, you loose !!")

#initial game setup
play_game = False
play_game_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game_input == "y":
    play_game = True

while play_game:
    clear()
    print(logo)
    #Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    for card in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.    
    #calculating initial score for both computer and setting user initial score to 0
    computer_score = calculate_score(computer_cards)
    user_score = 0
    user_game_on = True
    while user_game_on:
        user_score = calculate_score(user_cards)
        print(f"    Your cards are : {user_cards}, your current score is : {user_score}.")
        print(f"    Computer's first card is : {computer_cards[0]}.")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            user_game_on = False
        else:
            #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to                       #add another card to the user_cards List. If no, then the game has ended.
            draw_another_card_user_input = input("Do you want to pick another card ? Type 'y' to get another card, type 'n' to pass: ")
            if draw_another_card_user_input == 'y':
                user_cards.append(deal_card())
            else:
                user_game_on = False

    #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    if computer_score != 0:    #if it's not a blackjack for the computer
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    #Final cards revelation and the winner result
    print(f"    Your final hand: {user_cards}, final score: {user_score}.")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}.")
    compare(score_of_user= user_score,score_of_computer= computer_score)
    #Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show 
    #the logo from art.py.
    restart_game_input = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if restart_game_input == "n":
        play_game = False
