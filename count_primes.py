# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:34:24 2019

@author: SUNNY THAKUR
"""

import math
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True

def count_primes(num):
    count = 0
    for i in range(num):
        if is_prime(i):
            count += 1
    return count

import time
start_time = time.time()
print(count_primes(1000000))
print(time.time()-start_time)