#~ Sub-string divisibility
#~ Problem 43
#~ The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#~ Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#~ d2d3d4=406 is divisible by 2
#~ d3d4d5=063 is divisible by 3
#~ d4d5d6=635 is divisible by 5
#~ d5d6d7=357 is divisible by 7
#~ d6d7d8=572 is divisible by 11
#~ d7d8d9=728 is divisible by 13
#~ d8d9d10=289 is divisible by 17
#~ Find the sum of all 0 to 9 pandigital numbers with this property.
import math
import itertools


l = range(0,10)
sums=0
for i in itertools.permutations(l,10):
   n=sum([i[j]*10**j for j in range(0,10)])
   d234=int(n%(10**9) / 10**6)
   if d234%2!=0:
      continue;
   d234=int(n%(10**8) / 10**5)
   if d234%3!=0:
      continue;
   d234=int(n%(10**7) / 10**4)
   if d234%5!=0:
      continue;
   d234=int(n%(10**6) / 10**3)
   if d234%7!=0:
      continue;
   d234=int(n%(10**5) / 10**2)
   if d234%11!=0:
      continue;
   d234=int(n%(10**4) / 10**1)
   if d234%13!=0:
      continue;
   d234=int(n%(10**3))
   if d234%17!=0:
      continue;
   sums+=n
   print(sums,n)