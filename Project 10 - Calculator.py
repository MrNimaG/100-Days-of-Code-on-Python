import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2


functions = [add, subtract, multiply, divide]
operations = {}
keys = ['+', '-', '*', '/']

for item in range(4):
    operations[keys[item]] = functions[item]


answer = True
first_number = float(input("What's the first number? "))

while answer:
    chosen_operation = input(" + \n - \n * \n / \n Pick and operation: ")
    second_number = float(input("What's the next number? "))
    result = operations[chosen_operation](first_number, second_number)
    print(f"{first_number} {chosen_operation} {second_number} = {result}")
    continuation = input(f"Type \'y\' to continue calculation with {result}, or type \'n\' to start a new calculation: ")
    first_number = result
    if continuation == 'n':
        answer = False


