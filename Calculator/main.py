#Calculator
from art import logo
print(logo)

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

#First number that user inputs into the calculator
num1 = int(input("What's the first number?: "))

#Prints the operations that are available to do in the dictionary
for symbol in operations:
  print(symbol)

#User input for what operation to do and the second number
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

#Inputs the user input into the code below to get the answer
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")