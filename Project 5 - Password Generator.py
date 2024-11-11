import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ''
#
# chosen_result = []
# for i in range(0, nr_numbers):
#     chosen_result.append(random.choice(numbers))
#
# print(chosen_result)
#
# for i in range(0, nr_symbols):
#     chosen_result.append(random.choice(symbols))
#
# print(chosen_result)
#
# for i in range(0, nr_letters):
#     chosen_result.append(random.choice(letters))
#
# print(chosen_result)
#
# for i in range(0, len(chosen_result)):
#     password += chosen_result[i]
#
# print(password)
# random.shuffle(chosen_result)
#
# password = ''
#
# for i in range(0, len(chosen_result)):
#     password += chosen_result[i]
#
# print(password)

print("Your password will be made from totally 6 letters, 6 numbers and 6 symbols")
# First section of the password
password = ''

password1 = ''

password2 = ''

password3 = ''

section1 =[]

section2 =[]

section3 =[]

for i in range(0,2):
    section1.append(random.choice(letters))

for i in range(0,2):
    section1.append(random.choice(numbers))

for i in range(0, 2):
    section1.append(random.choice(symbols))

random.shuffle(section1)

for char in section1:
    password1 += char

# print(password1)

for i in range(0,2):
    section2.append(random.choice(letters))

for i in range(0,2):
    section2.append(random.choice(numbers))

for i in range(0, 2):
    section2.append(random.choice(symbols))

random.shuffle(section2)

for char in section2:
    password2 += char

# print(password2)

for i in range(0,2):
    section3.append(random.choice(letters))

for i in range(0,2):
    section3.append(random.choice(numbers))

for i in range(0, 2):
    section3.append(random.choice(symbols))

random.shuffle(section3)

for char in section3:
    password3 += char

# print(password3)

password = password1 + ' ' + password2 + ' ' + password3

print(f"Our suggested password is : {password}")



