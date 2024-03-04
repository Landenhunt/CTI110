# Landen Hunt
# 3/3/2024
# P2LAB2
# Write a program,Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers. 
n1 = float(input('Input first number: '))#input first number

n2 = float(input('Input second number: '))#input second number

n3 = float(input('Input third number: '))#input third number

n4 = float(input('Input fourth number: '))#input fourth number

average = (n1+n2+n3+n4)/4 #calculate input number average

product = n1*n2*n3*n4 # calculate input number product

print('product: {:.0f} average: {:.0f}'.format(round(product),round(average))) #print product and average using round function

print('product: {:.3f} average: {:.3f}'.format(product,average)) #print product and average value
