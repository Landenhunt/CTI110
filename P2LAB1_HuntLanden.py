# Landen Hunt
# 3/3/2024
# P2LAB1
# Write a program, that converts a cars gas mileage as the output for gas cost
mileage = float(input())
cost = float(input())

cost_20 = 20 / mileage * cost
cost_75 = 75 / mileage * cost
cost_500 = 500 / mileage * cost

print(f'{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}')
