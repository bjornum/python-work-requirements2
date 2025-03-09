# Part of Task 8: Simple Calculator Module

# class Calculator:

#     ## Initialise the calculater to take two numbers and a operator.
#     def __init__(self, number_one, number_two, operation):
#         self.number_one = number_one
#         self.number_two = number_two
#         self.operation = operation

def add(number_one, number_two):
    return number_one + number_two

def substract(number_one, number_two):
   return number_one - number_two

def multiply(number_one, number_two):
   return number_one * number_two

def divide(number_one, number_two):
    if number_one == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    elif number_two == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return number_one / number_two
