
import math
import itertools
import string


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

nArray =[[] for i in range(0,1000)]
fobj = open("p099_base_exp.txt")
i = 0
for line in fobj:
    nArray[i] = string.split(line.rstrip(),",")
    i += 1

fobj.close()

nPrimes = [[] for i in range (0,1000)]
i = 0
for n in nArray:
	nPrimes[i] = [ i+1, n[0], is_prime(n[0]), n[1], is_prime(n[1])]
	print (nPrimes[i])
	i += 1
   

def div_con_max(list, n):
	j = pl[n]