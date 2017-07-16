# -*- coding: utf-8 -*-
"""
@author: T3
"""

import math
startList = []
primes = [1]
top = input('Top of range = ')
for i in range(1,int(top)+1):
    startList.append(i)
for j in startList:
    count = 1
    index = int(math.floor(j/2+.5))
    for k in range (2,index+1):
        if math.gcd(j, k) != 1:
            count += 1
        else:
            if count == 1 and k == index:
                if primes[len(primes)-1] != j:
                    primes.append(j)
print(primes)