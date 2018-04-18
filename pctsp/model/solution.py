# module solution.py
#
# Copyright (c) 2018 Rafael Reis
#
"""
solution module - Implements Solution, a class that describes a solution for the problem.

"""
__version__="1.0"

import numpy as np
import copy
from random import shuffle

def random(pctsp, size):
    s = Solution(pctsp)
    length = len(pctsp.prize)

    if size: s.size = size

    cities = list(range(1, length, 1))
    shuffle(cities) # Shuffle in place
    s.route = [0] + cities # The city 0 is always the first    

    return s

class Solution(object):
    """
    Attributes:
       route (:obj:`list` of :obj:`int`): The list of cities in the visiting order
       size (:obj:`int`): The quantity of the first cities to be considered in the route list
       quality (:obj:`int`): The quality of the solution
    """

    def __init__(self, pctsp):
        self._route = []
        self.size = len(pctsp.prize) # Default size value is the total of cities
        self.quality = 0
        self.pctsp = pctsp
        self.prize = 0

    """
    Computes the quality of the solution.
    """
    def compute(self):
        self.prize = 0
        self.quality = 0
        for i,city in enumerate(self._route):
            if i < self.size:
                self.prize += self.pctsp.prize[city]
                if i > 0:
                    previousCity = self._route[i - 1]
                    self.quality += self.pctsp.cost[previousCity][city]
                if i + 1 == self.size:
                    self.quality += self.pctsp.cost[i][0]
            else:
                self.quality += self.pctsp.penal[city]

    def copy(self):
        return copy.copy(self)
    
    def swap(self, i, j):
        city_i = self._route[i]
        city_i_prev = self._route[i-1]
        city_i_next = self._route[(i+1) % self.size]
        
        city_j = self._route[j]

        self.quality = (self.quality
                - self.pctsp.cost[city_i_prev][city_i] - self.pctsp.cost[city_i][city_i_next]
                + self.pctsp.cost[city_i_prev][city_j] + self.pctsp.cost[city_j][city_i_next])
        self.prize = self.prize - self.pctsp.prize[city_i] + self.pctsp.prize[city_j]

        self._route[j], self._route[i] = self._route[i], self._route[j]

    def is_valid(self):
        return self.prize >= self.pctsp.prize_min

    def add_city(self):
        city_l = self._route[self.size - 1]
        city_add = self._route[self.size]        

        self.quality = (self.quality
            - self.pctsp.cost[city_l][0]
            + self.pctsp.cost[city_l][city_add]
            + self.pctsp.cost[city_add][0])
        
        self.size += 1
        self.prize += self.pctsp.prize[city_add]

    def remove_city(self, index):
        city_rem = self._route[index]
        city_rem_prev = self._route[index-1]
        city_rem_next = self._route[(index+1)%self.size]

        self.quality = (self.quality
            - self.pctsp.cost[city_rem_prev][city_rem] - self.pctsp.cost[city_rem][city_rem_next]
            + self.pctsp.cost[city_rem_prev][city_rem_next])
        self.prize -= self.pctsp.prize[city_rem]

        del self._route[index]        
        self._route.append(city_rem)

        self.size -= 1

    def remove_cities(self, quant):
        for i in range(self.size-quant,self.size):
            city_rem = self._route[i]
            city_rem_prev = self._route[i-1]

            self.quality -= self.pctsp.cost[city_rem_prev][city_rem]
            self.prize -= self.pctsp.prize[city_rem]

        city_rem = self._route[self.size-1]
        city_l = self._route[self.size-quant-1]
        self.quality = (self.quality - self.pctsp.cost[city_rem][0]
            + self.pctsp.cost[city_l][0])

        self.size -= quant

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, r):
        self._route = r
        self.compute()
