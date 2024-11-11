# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
# import art
print(art.logo)

bidders ={}
answer = True

while answer:
    name = input("What is your name?").lower()
    price = int(input("What is your bid? $"))
    bidders[name] = price
    question = input("Is there any other bidder? if 'yes' type yes.").lower()
    print('\n' * 50)
    if question == 'no':
        answer = False

highest_value = []
highest_key = []

for key in bidders:
    highest_value.append(bidders[key])
    highest_key.append(key)

highest_bid = max(highest_value)
highest_key_index = highest_value.index(highest_bid)
highest_bidder = highest_key[highest_key_index]


print(f"{highest_bidder} has the highest bid with bidding ${highest_bid}")

