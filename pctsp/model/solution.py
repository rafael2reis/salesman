# module solution.py
#
# Copyright (c) 2018 Rafael Reis
#
"""
solution module - Implements Solution, a class that describes a solution for the problem.

"""
__version__="1.0"

import numpy as np
from random import shuffle

def random(pctsp):
    s = Solution(pctsp)
    size = len(pctsp.prize)

    cities = list(range(1, size, 1))
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

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, r):
        self._route = r
        self.compute()
