# Landen Hunt
# 3/10/24
# P2HW1
# This calculates and displays travel expenses with aligned output and floating numbers.

# Get user input for budget and travel details
print('This program calculates and displays travel expenses')
user_budget = float(input('Please enter your budget:\n'))
print('Please enter travel destination:')
user_destination = input()
user_gas = float(input('How much do you think you will spend on gas?\n'))
user_accomodations = float(input('How much do you think you will spend on accommodations?\n'))
user_food = float(input('Last, how much do you think you will spend on food?\n'))

# Display travel expenses with aligned output
print('-------Travel Expenses-------')
print(f'{"Location:":<20}{user_destination}')
print(f'{"Initial Budget:":<20}${user_budget:.2f}')
print(f'{"Fuel:":<20}${user_gas:.2f}')
print(f'{"Accommodation:":<20}${user_accomodations:.2f}')
print(f'{"Food:":<20}${user_food:.2f}')
print('-----------------------------')
print()
total_expenses = user_gas + user_accomodations + user_food
print(f'{"Expenses added up:  ":<10}${total_expenses:.2f}')
remaining_balance = user_budget - total_expenses
print(f'{"Remaining Balance:  ":<10}${remaining_balance:.2f}')
