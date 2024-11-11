# import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards =[]
computer_cards = []




def welcome():
    print(art.logo)
    print("Welcome to the game of BlackJack!")

def card_for_user():
    # assigning a card to user's deck
    user_cards.append(random.choice(cards))

def card_for_computer():
    # assigning a card to computer's deck
    computer_cards.append(random.choice(cards))

def user_hand():
    print(f"Your Cards are: {user_cards}")
    print(f" Your current score is : {sum(user_cards)}")


def replay():
    answer = input(" Do you want to play another round? If yes type \'y\' and if not type \'n\'")
    return answer

outer_loop = True

while outer_loop:
    question1 = input("Do you want to play a round of Blackjack? Type \'y\' for yes and \'n\' for no ").lower()
    inner_loop = True
    user_cards = []
    computer_cards = []
    while inner_loop:
        continuation = True
        if question1 == 'y':
            print('\n' * 100)
            welcome()
            card_for_user()
            card_for_user()
            card_for_computer()
            user_hand()
            print(f"Computer\'s first card is: {computer_cards[0]}")
            if sum(user_cards) == 21:
                print("Won by Blackjack")
                question1 = ''
                inner_loop = False
                break
            else:
                while sum(user_cards) < 21:
                    answer2 = input(" Type \'y\' to get another card, Type \'n\' to pass: ").lower()
                    if answer2 == 'y':
                        card_for_user()
                        user_hand()
                        if sum(user_cards) > 21:
                            print("You overran and Lost")
                            question1 = ''
                            inner_loop = False
                            break
                        elif sum(user_cards) == 21:
                            print("Won by Blackjack")
                            question1 = ''
                            inner_loop = False
                            break
                    elif answer2 == 'n':
                        break
                    else:
                        print("Wrong input!!! Please try again")
            if sum(user_cards) > 21:
                question1 = ''
                inner_loop = False
                break
            elif sum(user_cards) == 21:
                question1 = ''
                inner_loop = False
                break
            print(f"Your final hand is: {user_cards} and your final score is: {sum(user_cards)}")
            while sum(computer_cards) <= 17:
                card_for_computer()
            if sum(computer_cards) == 21:
                print(f"Computer\'s final hand is: {computer_cards} with a final score of {sum(computer_cards)}")
                print("Computer has won by BlackJack")
                question1 = ''
                inner_loop = False
            elif sum(computer_cards) > 21:
                print(f"Computer\'s final hand is: {computer_cards} with a final score of {sum(computer_cards)}")
                print("Computer has over ran and you won")
                question1 = ''
                inner_loop = False
            elif sum(user_cards) < sum(computer_cards) < 21:
                print(f"Computer\'s final hand is: {computer_cards} with a final score of {sum(computer_cards)}")
                print("Computer has won")
                question1 = ''
                inner_loop = False
            elif sum(user_cards) == sum(computer_cards):
                print(f"Computer\'s final hand is: {computer_cards} with a final score of {sum(computer_cards)}")
                print("It\'s a draw")
                question1 = ''
                inner_loop = False
            else:
                print(f"Computer\'s final hand is: {computer_cards} with a final score of {sum(computer_cards)}")
                print("You won")
                question1 = ''
                inner_loop = False
        elif question1 == 'n':
            print('See you Next Time ')
            outer_loop = False
            break
        else:
            print('Wrong input! Please try again')
