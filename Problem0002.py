#~ Even Fibonacci numbers
#~ Problem 2
#~ Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#~ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#~ By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

f0 = 1
f1 = 2
f2 = 3

s = 2

while True:
	f0 = f1
	f1 = f2
	f2 = f0 + f1
	if f2 > 4000000:
		break
	else:
		if f2 % 2 == 0:
			s += f2
print (s)