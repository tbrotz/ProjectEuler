import math
import itertools
#~ import numpy as np
import fractions
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

p=set(sieve(1000000))
def is_prime(n):
    return n in p
pl=list(sieve(1000000))
#~ import random
 
#~ _mrpt_num_trials = 5 # number of bases to test
 
#~ def is_prime(n):
    #~ assert n >= 2
    #~ # special case 2
    #~ if n == 2:
        #~ return True
    #~ # ensure n is odd
    #~ if n % 2 == 0:
        #~ return False
    #~ # write n-1 as 2**s * d
    #~ # repeatedly try to divide n-1 by 2
    #~ s = 0
    #~ d = n-1
    #~ while True:
        #~ quotient, remainder = divmod(d, 2)
        #~ if remainder == 1:
            #~ break
        #~ s += 1
        #~ d = quotient
    #~ assert(2**s * d == n-1)
 
    #~ # test the base a to see whether it is a witness for the compositeness of n
    #~ def try_composite(a):
        #~ if pow(a, d, n) == 1:
            #~ return False
        #~ for i in range(s):
            #~ if pow(a, 2**i * d, n) == n-1:
                #~ return False
        #~ return True # n is definitely composite
 
    #~ for i in range(_mrpt_num_trials):
        #~ a = random.randrange(2, n)
        #~ if try_composite(a):
            #~ return False
 
    #~ return True # no base tested showed n as composite

def is_perm(n,i):
   return [str(n).count(str(i)) for i in range(0,10)]==[str(i).count(str(j)) for j in range(0,10)]

def is_palin(i):
   return (str(i)==str(i)[::-1])
def countt(plr,n):
   
   a = [plr.count(n.replace(i,"#")) for i in list(set(n)) if i!="#"]
   return (plr.count(n)+sum(a))

pl = [n for n in pl if max([str(n).count(str(i)) for i in range(0,10)])>=3]
plr=[]
for i in range(0,10):
   plr += [str(n).replace(str(i),"#") for n in pl if str(n).count(str(i))>=3]
#~ print(plr)
pls = set([])
for n in plr:
   if countt(plr,n)>=8:
      pls|=set([n])
plt = [[n.replace('#',str(i)) for i in range (0,10) if is_prime(int(n.replace('#',str(i))))] for n in list(pls)]
for xyz in plt:
	if len(xyz)>=8:
		print xyz
print(pls)




