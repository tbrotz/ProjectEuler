#~ Power digit sum
#~ Problem 16
#~ 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#~ What is the sum of the digits of the number 21000?

import math

print (2**1000)

p = 2 ** 1000

qs = 0

while p > 0:
	qs += p %10
	p /= 10

print qs