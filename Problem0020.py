#~ Factorial digit sum
#~ Problem 20
#~ n! means n * (n - 1) * ... * 3 * 2 * 1

#~ For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
#~ and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#~ Find the sum of the digits in the number 100!

def factorial(n):
	f = 0L
	f += n
	for i in range (1,n):
		f *= i
	return f
	
def digital_sum(n):
	p= n
	ds = 0
	while p > 0:
		ds += p %10
		p /= 10
		
	return ds
	
print (digital_sum(factorial(100)))