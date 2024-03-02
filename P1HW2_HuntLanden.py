# Landen Hunt
# 2/25/2024
# P1HW2
# create a program that does some basic math on numbers that are entered.
# Prints a message that shows what this program does
print('This program calculates and displays travel expenses')
# This gets the user to enter their input for their budget after displaying the message
user_budget = int(input('Please enter your budget:\n'))
# Prompts the user to enter where they are traveling Ex: Texas
print('Please enter travel destination:')
# User_destination is used to record the value for the destination
user_destination = input()
# This input instructs the user to input how much money they believe they will spend on gas
user_gas = int(input('How much do you think you will spend on gas?\n'))
# Input that instructs the user to list how much they think they will spend on accomodations
user_accomodations = int(input('How much do you think you will spend on accommodations?\n'))
# Input that instructs the user to list how much they think they will spend on food
user_food = int(input('Last how much do you think you will spend on food?\n'))
# Prints the word "'-------Travel Expenses-------'" as the title
print('-------Travel Expenses-------')
# Prints the word location and displays the value entered for the "user_Destination" input
print('Location:', user_destination)
# Prints the word initial budget and displays the value entered for the "user_budget" input
print('Initial Budget:', user_budget)
# Creates a blank space to seperate the "travel expenses" section from the bottom
print()
# Prints the word Fuel and the value for "user_gas"
print('Fuel:', user_gas)
# Prints the word Accomodation and the value for "user_accomodations
print('Accomodation:', user_accomodations)
# Prints the word Food and the value for "user_food"
print('Food:', user_food)
# Creates a blank space to seperate the "travel expenses" section from the bottom
print()
# Adds all of the inputs together and displays them next to the printed words
print('All expenses added up:', user_food + user_gas + user_accomodations)
# Subtracts the added up total from above from the budget set and entered
print('Remaining Balance:', user_budget - user_gas - user_accomodations - user_food)
