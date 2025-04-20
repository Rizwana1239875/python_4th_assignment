# MATH.CEAL(X)
# Return the smallest integer greater than or equal to x.
# if x is not a float, delegates to int(x).
# x=10.5
# print(math.ceil(x)) output is 11.0

import math
x=11.2
print(math.ceil(x))

x=12
print(math.ceil(x))

x=12.7
print(math.ceil(x))

# MATH.FABS(X)
# Return the absolute value of x.
# x=-10
# print(math.fabs(x)) output is 10.0

x=-10
print(math.fabs(x))

x=10
print(math.fabs(x))

# MATH.FACTORIAL(X)
# Return x factorial as an integer.Raises ValueError if x is not integral or is negative.
# x =5
# print(math.factorial(x)) output is 120

x = 5
print(math.factorial(x))

# MATH.FLOOR(X)
# Return the largest integer less than or equal to x.
# if x is not a float, delegates to int(x).
# x=10.5
# print(math.floor(x)) output is 10.0


x = 11.5
print(math.floor(x))

x = 11.8
print(math.floor(x))

x = 11
print(math.floor(x))


#MATH FSUM(ITERABLE)
# Return an accurate floating point sum of value in the iterable.

l = [10,20,30,40,50]
print(math.fsum(l))

# MATH.SQRT(X)
# Return the square root of x.
# x=16
# print(math.sqrt(x)) output is 4.0

print(math.sqrt(16))
print(math.sqrt(25))
print(math.sqrt(9))
print(math.sqrt(36))
print(math.sqrt(49))

