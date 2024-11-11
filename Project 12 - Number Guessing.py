# import art
import random

print(art.logo2)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

numbers = []

for i in range(100):
    numbers.append(i)
    i += 1
def game():
    chosen_number = random.choice(numbers)
    question1 = input("Choose a difficulty level. type 'easy' or 'hard': ").lower()
    if question1 == 'hard':
        user_lives = 5
        while True:
            if user_lives != 1 and user_lives != 0:
                print(f"you have {user_lives} attempts to correctly guess the number.")
                guess = int(input("Make a guess:"))
                if guess == chosen_number:
                    print("Bravo! You got it")
                    break
                elif guess < chosen_number:
                    print("Too Low!")
                    # print("Guess again!")
                    user_lives -= 1
                else:
                    print("Too High")
                    # print("Guess again!")
                    user_lives -= 1
                print("Guess again")
            elif user_lives == 1:
                print(f"you have {user_lives} attempt to correctly guess the number.")
                guess = int(input("Make a guess:"))
                if guess == chosen_number:
                    print("Bravo! You got it")
                    break
                elif guess < chosen_number:
                    print("Too Low!")
                    user_lives -= 1
                else:
                    print("Too High")
                    user_lives -= 1
            else:
                print("You ran out of attempts")
                break
    elif question1 == 'easy':
        user_lives = 10
        while True:
            if user_lives != 1 and user_lives != 0:
                print(f"you have {user_lives} attempts to correctly guess the number.")
                guess = int(input("Make a guess:"))
                if guess == chosen_number:
                    print("Bravo! You got it")
                    break
                elif guess < chosen_number:
                    print("Too Low!")
                    # print("Guess again!")
                    user_lives -= 1
                else:
                    print("Too High")
                    # print("Guess again!")
                    user_lives -= 1
                print("Guess again")
            elif user_lives == 1:
                print(f"you have {user_lives} attempt to correctly guess the number.")
                guess = int(input("Make a guess:"))
                if guess == chosen_number:
                    print("Bravo! You got it")
                    break
                elif guess < chosen_number:
                    print("Too Low!")
                    user_lives -= 1
                else:
                    print("Too High")
                    user_lives -= 1
            else:
                print("You ran out of attempts")
                break
    else:
        print("Wrong Input")


game()