n1 = float(input('Input first number: '))#input first number

n2 = float(input('Input second number: '))#input second number

n3 = float(input('Input third number: '))#input third number

n4 = float(input('Input fourth number: '))#input fourth number

average = (n1+n2+n3+n4)/4 #calculate input number average

product = n1*n2*n3*n4 # calculate input number product

print('product: {:.0f} average: {:.0f}'.format(round(product),round(average))) #print product and average using round function

print('product: {:.3f} average: {:.3f}'.format(product,average)) #print product and average value
