#~ Summation of primes
#~ Problem 10
#~ The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#~ Find the sum of all the primes below two million.




from math import sqrt
 
 
def sieve(limit):
	is_prime = [True] * limit
	is_prime[0] = is_prime[1] = False
	for i in range(2, int(sqrt(limit) + 1)):
		if is_prime[i]:
			for j in range(i * i, limit, i):
				is_prime[j] = False
	return (is_prime)

sum = 0
count = 0
APrimes = sieve(2000000)
l =  len(APrimes) - 1
for i in range (0, l ):
	if APrimes[i]:
		sum += i			

print (sum)