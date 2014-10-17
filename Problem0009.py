#~ Special Pythagorean triplet
#~ Problem 9
#~ A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#~ a2 + b2 = c2
#~ For example, 32 + 42 = 9 + 16 = 25 = 52.

#~ There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#~ Find the product abc.
i = 1
while True:
	j = i + 1
	while True:
		k = j + 1
		while True:
			if i * i + j * j == k * k:
				print (str(i) + "   " + str(j) + "   " + str(k) + "   " + str(i + j + k))
				print (i * j  * k)
				if (i + j + k == 1000):
					exit()
			if i + j + k > 1000:
				break
			k +=1
		j += 1
		if i + j > 1000:
			break
	i += 1
	if i > 1000:
		break