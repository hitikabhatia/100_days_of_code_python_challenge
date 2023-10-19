from replit import clear
from art import logo

#Add function
def add(n1, n2):
    return n1 + n2
#Subtract function
def subtract(n1, n2):
    return n1 - n2
#Multiply function
def multiply(n1, n2):
    return n1 * n2
#Divide function
def divide(n1, n2):
    return n1 / n2

#operations dictionary
operations = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide,
             }

#Calculator function
def my_digital_calculator():
    print(logo)
    #input the first number
    number1 = float(input("What's the first number ?: "))
    for key in operations:
        print(key)
    
    should_continue = True
    
    while should_continue == True:
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        calculation_result = calculation_function(n1 = number1,n2 = number2)
        print(f"{number1} {operation_symbol} {number2} = {calculation_result}")
        continue_with_result = input(f"Type 'y' to continue calculating with {calculation_result}, or type 'n' to start a new calculation: ")
        if continue_with_result == "n":
            should_continue = False
            clear()
            #recursive call to my calculator function
            my_digital_calculator()
        else:
            number1 = calculation_result

#first call to the my digital calculator function.
my_digital_calculator()
