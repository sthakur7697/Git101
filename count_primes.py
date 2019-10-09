# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:31:46 2019

@author: SUNNY THAKUR
"""
import time
start_time = time.time()

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)

print(count_primes(10000))
print(time.time()-start_time)

# 3.5885233879089355
# 3.9199440479278564
