#~ Goldbach's other conjecture
#~ Problem 46
#~ It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#~ 9 = 7 + 2×12
#~ 15 = 7 + 2×22
#~ 21 = 3 + 2×32
#~ 25 = 7 + 2×32
#~ 27 = 19 + 2×22
#~ 33 = 31 + 2×12

#~ It turns out that the conjecture was false.

#~ What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math
import itertools


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

p=set(sieve(100000))
def is_prime(n):
    return n in p
pl=list(sieve(100000))


l=set([2*i-1 for i in range(3,100000) if not is_prime(2*i-1)])

for i in pl:
   j=1
   while (i+2*j**2)<100000:
      if i+2*j**2 in l:
         l.remove(i+2*j**2)
      j+=1
   print (i)
   if min(l)<i:
      print ("sol:",min(l))
   
