#~ Highly divisible triangular number
#~ Problem 12
#~ The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#~ 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#~ Let us list the factors of the first seven triangle numbers:

 #~ 1: 1
 #~ 3: 1,3
 #~ 6: 1,2,3,6
#~ 10: 1,2,5,10
#~ 15: 1,3,5,15
#~ 21: 1,3,7,21
#~ 28: 1,2,4,7,14,28
#~ We can see that 28 is the first triangle number to have over five divisors.

#~ What is the value of the first triangle number to have over five hundred divisors?
	
n1 = 1
n2 = 2
c1 = 1
c2 = 2

while True:
	n1 = n2
	c1 = c2
	n2 += 1
	c2 = 0
	for i in range(1,n2+1):
		if n2 % i == 0:
			c2 += 1
			
	if c1 * c2 >= 500:
		n3 = int(n1*n2/2)
		c3 = 0
		for i in range(1,n3+1):
			if n3 % i == 0:
				c3 += 1
		print ([c1, n1, c2, n2, c3, n3, c1*c2])
		if c3 > 500:
			exit()
		