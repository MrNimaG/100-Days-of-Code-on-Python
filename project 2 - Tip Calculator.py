print("Welcome to my Tip Calculator")
Bill = float(input("What was the total bill?\n$"))
Tip = float(input("How much tip would you like to give?10, 12 or 15?\n"))
Number_of_People = int(input("How many people to split the bill?\n"))

Each_Person_Pay = round((Bill / Number_of_People) * (1 + Tip / 100) , 2)
print(f"Each person should pay : ${Each_Person_Pay}")


