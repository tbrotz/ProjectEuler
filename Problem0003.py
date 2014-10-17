#~ Largest prime factor
#~ Problem 3
#~ The prime factors of 13195 are 5, 7, 13 and 29.

#~ What is the largest prime factor of the number 600851475143 ?

number = 600851475143
factor = 2

while number > 1:
	if number % factor == 0:
		print (factor)
		number = number/factor
	else:
		factor += 1
	