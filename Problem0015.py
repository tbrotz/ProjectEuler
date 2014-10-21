#~ Lattice paths
#~ Problem 15
#~ Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


#~ How many such routes are there through a 20*20 grid?

def factorial(n):
	f = 0L
	f += n
	for i in range (1,n):
		f *= i
	return f

def choose(n,k):
	c = 0L
	c += factorial (n)
	c /= factorial(k)
	c /= factorial(n-k)
	return c

print (choose(40,20))
