import math

L = [[0 for i in range (0,10)] for j in range (0,10000)]

L2 = []

for i in range (0,10000):
	n = i**3
	for j in range (0,10):
		
		L[i][j] = str(n).count(str(j))
		
	if L.count(L[i]) == 5:
		#~ print (n)
		L2 += [L[i]]
		
for i in range (0,10000):
	n = i**3
	x = []
	for j in range (0,10):
		
		x += [str(n).count(str(j))]
	if L2.count(x) >= 1:
		print (n)
		exit()
