# Swapping two number using third variable

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print('Before swapping numbers are: {0} and {1}'.format(a, b))

temp = a
a = b
b = temp

print('After swapping numbers are: {0} and {1}'.format(a, b))