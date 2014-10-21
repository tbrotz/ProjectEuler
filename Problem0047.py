#~ Distinct primes factors
#~ Problem 47
#~ The first two consecutive numbers to have two distinct prime factors are:

#~ 14 = 2 * 7
#~ 15 = 3 * 5

#~ The first three consecutive numbers to have three distinct prime factors are:

#~ 644 = 2^2 * 7 * 23
#~ 645 = 3 * 5 * 43
#~ 646 = 2 * 17 * 19.

#~ Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

import math
import itertools


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)

p=set(sieve(1000000))
def is_prime(n):
    return n in p
pl=list(sieve(1000000))

min=1000000
l=[set([]) for i in range(0,1000000)]
for i in pl:
   j=1
   while (j*i<1000000):
      l[j*i]|=set([i])
      if len(l[j*i])==4:
         if len(l[i*j-1])==4:
            if len(l[i*j-2])==4:
               if len(l[i*j-3])==4:
                  if (i*j-1)<min:
                     min=i*j-3
      j+=1
   
print(min)