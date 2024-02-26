# Landen Hunt
# 2/25/2024
# P1HW2
# create a program that does some basic math on numbers that are entered.
print('This program calculates and displays travel expenses')
user_budget = int(input('Please enter your budget:\n'))
print('Please enter travel destination:')
user_destination = input()
user_gas = int(input('How much do you think you will spend on gas?\n'))
user_accomodations = int(input('How much do you think you will spend on accommodations?\n'))
user_food = int(input('Last how much do you think you will spend on food?\n'))
print('-------Travel Expenses-------')
print('Location:', user_destination)
print('Initial Budget:', user_budget)
print()
print('Fuel:', user_gas)
print('Accomodation:', user_accomodations)
print('Food:', user_food)
print()
print('All expenses added up:', user_food + user_gas + user_accomodations)
print('Remaining Balance:', user_budget - user_gas - user_accomodations - user_food)

