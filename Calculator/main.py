#Calculator
from art import logo

#Add
def add(n1, n2):
  return n1 + n2 

#Subtract
def subtract(n1, n2):
  return n1 - n2 

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2 

#Dictionary with the different operation functions
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

#Recursion so if you say 'n', you can do a brand new calculator function  
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
            print(symbol)
            
    continue_calc = True
    #While loop to continue operations until you select no
    while continue_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n'to exit.: ") == "y":
            num1 = answer
        else:
            continue_calc = False
            calculator()
            
calculator()