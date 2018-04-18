# module ilocal_search.py
#
# Copyright (c) 2018 Rafael Reis
#
"""
ilocal_search module - Implements Iterate Local Search algorithm.

"""
__version__="1.0"

import numpy as np
import random

def ilocal_search(s):
    h = s.copy()
    best = s.copy()
    times = random.sample(range(1000, 2000), 10)    

    while len(times) > 0:
        time = times.pop()
        t = 0
        while t < time:
            r = tweak(s.copy())
            if r.quality < s.quality:
                s = r
            t += 1
        if s.quality < best.quality:
            best = s
        h = newHomeBase(h, s)
        s = perturb(h)
    
    return best

def tweak(solution):
    s = solution

    s_1 = m1(solution.copy())
    s_2 = m2(solution.copy())
    
    if (s_1 and s_1.quality < solution.quality 
        and (not s_2 or s_1.quality < s_2.quality)
        and s_1.is_valid()):
        s = s_1
    elif (s_2 and s_2.quality < solution.quality
        and (not s_1 or s_2.quality < s_1.quality)
        and s_2.is_valid()):
        s = s_2
    else:
        s_3 = m3(solution.copy())
        if (s_3 and s_3.quality < solution.quality
            and s_3.is_valid()):
            s = s_3

    return s

def newHomeBase(h, s):
    if s.quality <= h.quality:
        return s
    else:
        return h

def perturb(solution):
    if solution.size > 5:
        quant = int(solution.size/5)
        solution.remove_cities(quant=quant)

    return solution

def m1(solution):
    size = solution.size
    length = len(solution.route)

    if size < length:
        i = random.randrange(1, size)
        j = random.randrange(size, length)
        solution.swap(i, j)

def m2(solution):
    if solution.size > 1:
        i = random.randrange(1, solution.size)
        solution.remove_city(index=i)

def m3(solution):
    if solution.size < len(solution.route):
        solution.add_city() 
