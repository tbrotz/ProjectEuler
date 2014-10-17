#~ Largest palindrome product
#~ Problem 4
#~ A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

#~ Find the largest palindrome made from the product of two 3-digit numbers.

def is_palin(a):
	s = str(a)
	l = len(s)
	for i in range (0, l):
		if s[i] != s[(-1 * i) - 1]:
			return False
	return True

max = 0	
for i in range (100, 1000):
	for j in range (i, 1000):
		if is_palin(i*j) and i*j > max:
			max = i*j
			#~ print(str(i*j) + "\t" + str(i) + "\t" + str(j))
print ("\n\n\n" + str(max))