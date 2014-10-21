from fractions import Fraction



l=[]
for i in range(1,34):
	l+=[1,2*i,1]

n=Fraction(1)
for k in reversed(l[:-1]):
	n=k+Fraction(1,n)
print (sum([int(i) for i in (str((2+1/n).numerator))]))