import math
import random
# Conner Zhao
name = input('Please enter your name')
smalDec = float(input(name + ' Please type small decimal number'))
largDec = float(input(name + ' Please type large decimal number'))
ranDec = random.uniform(smalDec, largDec)
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* ranDec**3
print("Your radius for the sphere is " + V)