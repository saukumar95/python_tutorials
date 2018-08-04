import cmath
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

# Calculating discrimant

d = (b**2)-(4*a*c)

# two solutions

sol1 = (-b - cmath.sqrt(d)/(2*a))
sol2 = (-b + cmath.sqrt(d/(2*a)))

print('Solutions are {0} {1}'.format(sol1, sol2))
