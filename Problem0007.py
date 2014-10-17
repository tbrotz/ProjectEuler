#~ 10001st prime
#~ Problem 7
#~ By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#~ What is the 10 001st prime number?

from math import sqrt

		
def sieve(limit):
	is_prime = [True] * limit
	is_prime[0] = is_prime[1] = False
	for i in range(2, int(sqrt(limit) + 1)):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return (is_prime)


t = 1000
while True:
	APrimes = sieve(t)
	print (t)
	count = 0
	l =  len(APrimes) - 1
	for i in range (0, l ):
		if APrimes[i]:
			count += 1
		if count == 10001:
			print(i)
			exit()
	t *=4

print (sum)

