# import all import functions needed
import random
# import art
# import game_data

data = game_data.data

# this how I can take the number of followers from the selected dictionary from the list
# print(data[0]["follower_count"])

A = random.choice(data)
B = random.choice(data)
print(A["follower_count"])
print(B["follower_count"])
score = 0
result = True

def compare():
    global score
    global result
    winning_answer = ""
    if A["follower_count"] > B["follower_count"]:
        winning_answer = 'a'
    else:
        winning_answer = 'b'
    guess = input("Who has more followers? Type 'A' or 'B':   ").lower()
    if guess == winning_answer:
        score += 1
        print(f"You're right! Current Score is {score}")
    else :
        print(art.logo)
        print(f"Sorry, That's wrong. Final score is {score}")
        result = False

while A != B and result:
    print(art.logo)
    print(f"Compare A: {A["name"]}, {A["description"]}, from {A["country"]}.")
    print(art.vs)
    print(f"Against B: {B["name"]}, {B["description"]}, from {B["country"]}.")
    compare()
    if result:
        A = B
        B = random.choice(data)
        print("\n" * 50)
