def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


Operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,}

def calculator():
    should_accumulate = True
    num1 = float(input("Enter the first number: "))
    while should_accumulate:

        for symbol in Operations:
            print(symbol)
        chosen_operator = input('Enter the operator of your choice:')

        num2 = float(input("Enter the second number: "))

        answer = Operations[chosen_operator](num1, num2)
        print(f"{num1} {chosen_operator} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()